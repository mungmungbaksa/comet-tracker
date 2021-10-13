import math 
def sqrt(x): #음수의 제곱근으로 허수를 출력해준다.
    if x>=0:
        return math.sqrt(x)
    else:
        return complex(0,math.sqrt(-x))