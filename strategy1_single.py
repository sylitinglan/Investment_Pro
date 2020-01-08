'''一个实现期权单腿策略的py文件'''

###############单腿交易################
#单腿交易分为以下四种：买入看涨，卖出看涨，买入看跌，卖出看跌
import matplotlib.pyplot as plt
from black_scholes import vol_list
from option_api import ETF_fund,s0_list,T_list,ETF_option
import numpy as np
import pandas as pd

E1=2.60

def draw_vol_timeseries(vol_list):#画隐含波动率时序图
    a=list(reversed(vol_list))
    ETF_timeseries=pd.to_datetime(ETF_option['trade_date'])
    plt.plot(ETF_timeseries,a)
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    plt.xlabel("时间") #X轴标签  
    plt.ylabel("期权隐含波动率")
    plt.savefig('./期权隐含波动率时序图.png')
    plt.show()
    
#draw_vol_timeseries(vol_list)

#隐含波动率时序图如果无法说明当前隐含波动率的历史地位的话，就运行下一个分级函数。

def vol_rank(vol_list):
    a=vol_list.copy()
    a.sort(reverse=True)
    if vol_list[0] >= a[int(len(a)*0.3)]:
        print("隐含波动率较大，卖出") 
    elif vol_list[0] <= a[int(len(a)*0.7)]:
        print("隐含波动率较小，买入") 
    else:
        print("暂不做交易") 
    
vol_rank(vol_list)
