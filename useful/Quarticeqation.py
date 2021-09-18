import math
import bettersqrt
def Quartric(a,b,c,d,e):
    P=b/(4*a)
    Q=(2*c)/(3*a)
    R=c*c-3*b*d+12*a*e
    S=2*c*c-9*b*c*d+27*a*d+27*e*b*b-72*a*c*e
    T=(-(b*b*b)/a*a*a)+((4*b*c)/a*a)-(8*d/a)
    temp=math.pow(S+bettersqrt.sqrt((-4*R*R*R)+S*S),3)
    V=((math.pow(2,1/3)*R)/(3*a*temp))+(temp/3*math.pow(2,1/3)*a)
    temp1=(bettersqrt.sqrt(4*P*P-Q+V))/2
    temp2=bettersqrt.sqrt(8*P*P-2*Q-V-(T/(4*bettersqrt.sqrt(4*P*P-Q+V))))/2
    return [-P-temp1-temp2,-P-temp1+temp2,-P+temp1-temp2,-P+temp1+temp2]