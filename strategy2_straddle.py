'''期权跨式交易'''
from option_api import s0_list
import numpy as np
import matplotlib.pyplot as plt
####change the calue before you start run this file###
E1=3.10
E2=3.20
##############
S1=[]
straddle_long=[]#买入跨期交易
S_indice1=0
#if self.option_type=="EU_Call":
for i in np.arange(min(s0_list),max(s0_list),0.001):#
    S1.append(i)
    k=max(S1[S_indice1]-E1,0)+max(E2-S1[S_indice1],0)
    straddle_long.append(k)
    S_indice1=S_indice1+1
straddle_put=[-1*i + 10 for i in straddle_long]  #卖出跨式期权          
plt.plot(S1,straddle_long)
plt.plot(S1,straddle_put)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.axvline(x=s0_list[0],ls=":",c="red")
plt.xlabel("股票到期价格S(T)") #X轴标签  
plt.ylabel("ETF跨式/宽跨式期权到期收益")
#plt.savefig("./跨式期权到期收益.png")  
plt.show()