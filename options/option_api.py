

import tushare as ts
import pandas as pd
import numpy as np

'''期权日线行情信息转化'''
END_DATE='20191225'#当前/回测截止点
START_DATE='20190807'#期权上市时间点or自行设定
pro = ts.pro_api('ca31579fa28d0b4530ea43b3457a10a44f36020f73e94009a54207ac')
df = pro.opt_basic(exchange='SSE', fields='ts_code,name,exercise_type,list_date,delist_date')
ETF_option = pro.opt_daily(ts_code="10001910.SH", start_date=START_DATE, end_date=END_DATE)#期权基本数据调取，空格内填上自己想要的期权的代码
ETF_fund = pro.fund_daily(ts_code='510050.SH', start_date=START_DATE, end_date=END_DATE)#50ETF基金,end_date更新到最新日期
#df.to_excel("./所有期权合约列表.xlsx")

DEAD_LINE='20200624'#期权到期日


#注：我看见网上有人说波动率的计算要用到180个交易日的基金收益率数据。
# 所以以后优化程序的时候希望能够实现获取当钱日期向前提180天的抓取数据代码
#df.to_excel("./50ETF期权合约列表.xlsx")#存储数据以备查证

#1998	10001937.SH	华夏上证50ETF期权2003认购2.60	欧式	20190807	20200325

def cal_sigma(option_info,ETF_info):
    ret=np.log(ETF_info['close'])
    ret=np.diff(ret)#求出对数收益率(日)
    #ret_monthly=ret-ret.shift(30)#月收益率
    #ret_yearly=ret-ret.shift(365)#年收益率
    s=np.std(ret)#日波动率
    sigma=s/(1/250)**0.5#日波动率
    #sigma=s_monthly/(1/12)**0.5#月波动率
    #sigma_yearly=s_yearly/1**0.5#年波动率
    return sigma

T_list=[]
def cal_maturity(option_info,end_date):#计算期权已经交易的时间之内的成熟期限
    option_date=pd.to_datetime(option_info['trade_date'])
    end_date=pd.to_datetime(end_date)
    for i in range(option_info.shape[0]):
        T=(end_date-option_date[i]).days/365
        T_list.append(T)
    return T_list

s0_list=ETF_fund['close'].tolist()
c0_list=ETF_option['close'].tolist()

#print(s0_list)#获取ETF基金的当前价格
#sigma_list=[]

sigma=cal_sigma(ETF_option,ETF_fund)
cal_maturity(ETF_option,DEAD_LINE)
    #sigma_list.append(sigma)
print(sigma)
#ETF_price=option.valuation_class(s01,E1,rate1,T1,sigma1,153,type="Call")

#print(ETF_price.EU_option())
#print(sigma1)

#	10001847.SH	华夏上证50ETF期权1912认购2.60	欧式	20190507	20191225

#myoption=option.valuation_class(0.4232,0.4199,0.0268,0.419,0.0504,153,type="Call")
#print(myoption.EU_option())

#if __name__ == '__main__':
#    option_transform(option_info,ETF_info,end_date)
