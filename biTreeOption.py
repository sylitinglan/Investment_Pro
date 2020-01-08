import math
import numpy as np
def nCr(n,r):
    f=math.factorial
    return f(n)/(f(r)*f(n-r))
class valuation_class(object):
    '''期权的二叉树模型'''
    def __init__(self,s0,E,rate,T,sigma,N,type=""):
        self.s0=s0#现价
        self.E=E#执行价格
        self.rate=rate#利率
        self.T=T#期限
        self.sigma=sigma#波动率
        self.N=N#结点数
        self.type=type
    def EU_option(self):
        '''欧式看涨or看跌期权的定价计算函数'''
        time=self.T/self.N
        u=math.exp(self.sigma*time**0.5)
        d=math.exp(-self.sigma*time**0.5)
        p=(math.exp(self.rate*time)-d)/(u-d)
        #payment=0
        lattice=np.zeros([self.N+1,self.N+1])
        for i in range(self.N+1):
            if self.type=="Call":
                lattice[self.N,i]=max(((self.s0*u**i)*d**(self.N-i)-self.E),0)
                lattice[self.N,i]=round(lattice[self.N,i],4)
            elif self.type=="Put":
                lattice[self.N,i]=max((self.E-(self.s0*u**i)*d**(self.N-i)),0)
        for i in range(self.N-1,-1,-1):
            for j in range(0,i+1):
                lattice[i,j]=math.exp(-self.rate*time)*(p*lattice[i+1,j+1]+(1-p)*lattice[i+1,j])
                lattice[i,j]=round(lattice[i,j],4)
        price=lattice[0,0]
        return price#,lattice#（三角形矩阵可以选择性输出）
    def AM_option(self):
        '''美式看涨or看跌期权的定价计算函数'''
        time=self.T/self.N
        u=math.exp(self.sigma*time**0.5)
        d=math.exp(-self.sigma*time**0.5)
        p=(math.exp(self.rate*time)-d)/(u-d)
        #payment=0
        lattice=np.zeros([self.N+1,self.N+1])
        for i in range(self.N+1):
            if self.type=="Call":
                pass#美式看涨期权的公式以后再写
            elif self.type=="Put":
                lattice[self.N,i]=max((self.E-(self.s0*u**i)*d**(self.N-i)),0)
        for i in range(self.N-1,-1,-1):
            for j in range(0,i+1):
                lattice[i,j]=max((self.E-(self.s0*u**i)*d**(i-j)),(math.exp(-self.rate*time)*(p*lattice[i+1,j+1]+(1-p)*lattice[i+1,j])))
                lattice[i,j]=round(lattice[i,j],4)
        price=lattice[0,0]
        return price#,lattice#（三角形矩阵可以选择性输出）

#myoption=valuation_class(50.0,60.0,0.03,1,0.2,100,type="Put")
#print(myoption.AM_option())
            

#再见了


