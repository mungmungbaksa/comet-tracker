import math
from sympy import Symbol, solve , Abs
def Quartric(a,b,c,d,e): # 4차방정식의 근의 공식으로 허근을 제외한 근을 구하는 프로그램이다.
    x=Symbol('x')
    Quartriceq= a*x**4 + b*x**3 + c*x**2 + d*x + e
    anslist=solve(Quartriceq)
    realanslist=[]
    for x in anslist:
        if x==Abs(x):
            realanslist.append(float(x))
    return realanslist