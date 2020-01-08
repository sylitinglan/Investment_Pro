'''这是一个获取指定时间区间内可供交易的日期，并将它转换成聚宽认可的日期形式'''
import datetime
import tushare as ts
token="ca31579fa28d0b4530ea43b3457a10a44f36020f73e94009a54207ac"
ts.set_token(token)
pro = ts.pro_api()

trade_date_list=[]
def get_trade_date(STARTDATE,ENDDATE):
    date_list=pro.trade_cal(exchange='SSE'and'SZSE', start_date=STARTDATE, end_date=ENDDATE,is_open='1')
    for i in range(len(date_list)-1):#转换成聚宽认可的形式
        date_list['cal_date'][i]=datetime.datetime.strptime(date_list['cal_date'][i],'%Y%m%d')
        a=datetime.datetime.strftime(date_list['cal_date'][i],'%Y-%m-%d')
        a=date_list['cal_date'][i]
        trade_date_list.append(a.strftime('%Y-%m-%d'))
    return trade_date_list
    #return trade_date_list

#STARTDATE='20160101'
#ENDDATE='20180101'
#print(get_trade_date(STARTDATE,ENDDATE))
#date_list=pro.trade_cal(exchange='SSE', start_date=STARTDATE, end_date=ENDDATE,is_open='1')
#print(date_list)
if __name__ == '__main__':
    get_trade_date("20160101","20180101")#在这里搞出序列
    
