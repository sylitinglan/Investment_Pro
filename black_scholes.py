from math import log,sqrt,exp
import math
from scipy.stats import norm
import pandas as pd
import numpy as np
from option_api import T_list,s0_list,sigma,c0_list

#here define your variables
E=2.95
rate=0.0268#无风险收益率
it=50#迭代
q=.0#是否分红？
type="Call"#事先声明平凡期权的种类
#c0=1.0231#期权当前收盘价
np.seterr(invalid='ignore')
class BLS_OPTION(object):
    '''BS期权模型'''
    def __init__(self,s0,E,rate,T,sigma,q,type=""):
        self.s0=s0
        self.E=E
        self.rate=rate
        self.T=T
        self.sigma=sigma
        self.q=q
        self.type=type
        self.d1=(log(s0/E)+(rate-q+0.5*sigma**2)*T)/(sigma*sqrt(T))
        self.d2=(log(s0/E)+(rate-q-0.5*sigma**2)*T)/(sigma*sqrt(T))
    def bls_price(self):
        if type=="Call":
            price=self.s0*exp(-self.q*self.T)*norm.cdf(self.d1)-self.E*exp(-self.rate*self.T)*norm.cdf(self.d2)
        #return price
        elif type=="Put":
            price=self.E*exp(-self.rate*self.T)*norm.cdf(-self.d2)-self.s0*exp(-self.q*self.T)*norm.cdf(-self.d1)
        return price
    def bls_vega(self):#Greeks:vega
        vega=norm.cdf(self.d1)*sqrt(self.T)
        return vega
    #def bsm_imp_vol_newton(self,it,c0):#计算隐含波动率，c0为期权的实时收盘价
        #imp_vol=self.sigma
        #for i in range(it):
            #self.sigma-=(self.bls_price()-c0)/self.bls_vega()
        #imp_vol=self.sigma
        #return imp_vol
    def bls_delta(self):
        if type=="Put":
            delta=norm.cdf(self.d1)
        else:
            delta=norm.cdf(self.d1)-1
        return delta
    def bls_gamma(self):
        gamma=exp(-self.d1*self.d1*0.5)/self.sigma/self.s0/sqrt(2*math.pi*self.T)
        return gamma
    def bls_theta(self):
        if type=="Put":
            theta=-0.5*exp(-0.5*self.d1*self.d1)*self.sigma*self.s0/sqrt(2*self.T*math.pi)-self.rate*self.E*exp(-self.rate*self.T)*norm.cdf(self.d2)
        elif type=="Call":
            theta=-0.5*exp(-0.5*self.d1*self.d1)*self.sigma*self.s0/sqrt(2*self.T*math.pi)+self.rate*self.E*exp(-self.rate*self.T)*norm.cdf(self.d2)
        return theta
    def bls_rho(self):
        if type=="Put":
            rho=self.E*self.T*exp(-self.rate*self.T)*norm.cdf(self.d2)
        elif type=="Call":
            rho=-self.E*self.T*exp(-self.rate*self.T)*norm.cdf(-self.d2)
        return rho
def bsm_imp_vol_newton(s0,E,rate,T,sigma_est,q,it,c0):#计算隐含波动率，c0为期权的实时收盘价
    for i in range(it):
        sigma_est-=(BLS_OPTION(s0,E,rate,T,sigma_est,q,type).bls_price()-c0)/BLS_OPTION(s0,E,rate,T,sigma_est,q,type).bls_vega()
    return sigma_est

#creat Greeks list:
theta_list=[]
gamma_list=[]
vega_list=[]
rho_list=[]
delta_list=[]
vol_list=[]




for i in range(len(T_list)):
    hehe=BLS_OPTION(s0_list[i],E,rate,T_list[i],sigma,q,type=type)
    theta_list.append(hehe.bls_theta())
    gamma_list.append(hehe.bls_gamma())
    vega_list.append(hehe.bls_vega())
    rho_list.append(hehe.bls_rho())
    delta_list.append(hehe.bls_delta())
    sigma_est=1#????#以后再议
    vol_list.append(bsm_imp_vol_newton(s0_list[i],E,rate,T_list[i],sigma_est,q,it,c0_list[i]))



   

#print(T_list)
print(vol_list)
#print(delta_list)
#print(gamma_list)
#print(vega_list)
#print(rho_list)
