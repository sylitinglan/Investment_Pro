'''get stock returns of hs300'''
import pandas as pd
import numpy as np
import os
from jqdatasdk import *
import jqdatasdk
jqdatasdk.auth('17812137093','Sy16241098')
from get_trade_date import get_trade_date
#STARTDATE='20160101'
STARTDATE='20160101'
ENDDATE='20200101'
#ENDDATE='20200101'
trade_date_list=get_trade_date(STARTDATE,ENDDATE)
#######获取沪深300股票列表
stocks = get_index_stocks('000300.XSHG')
for tradeDate in trade_date_list:
    get_price(security, start_date=tradeDate, end_date=tradeDate, frequency='daily', fields=None, skip_paused=False, fq='pre', count=None, panel=True, fill_paused=True)
    pass

print(stocks)