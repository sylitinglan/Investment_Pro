import jqdatasdk
jqdatasdk.auth('17812137093','Sy16241098')
from jqdatasdk.alpha101 import *
import pandas as pd
from get_trade_date import get_trade_date

STARTDATE='20160101'
ENDDATE='20180101'
trade_date_list=get_trade_date(STARTDATE,ENDDATE)
#test_date=create_assist_date("2016-01-01","2020-01-05")


#get worldquant 101 alpha
for i in range(len(trade_date_list)-1):
    df=pd.DataFrame()
    df.append(alpha_001(trade_date_list[i],'000300.XSHG'))
    pass
#我们从一个dataframe中选取一列series1.
series1=data.pop('day')
#为df1添加一个列，第一个0我们可以改变选择你想插入的位置，第二个可以选择你想要的名字
df.insert(0,'series1',series1)
#对这一列赋值
#df['series1']=series1

