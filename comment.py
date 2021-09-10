import math
import matplotlib

def sqrt(x):
    return math.sqrt(x)
def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    return math.tan(x)

def defm(x,y,z,st,ct,so,co):
    return pow(ct*(co*x-so*z),2)-2*ct*st(co*x-so*z)*y+pow(st*y,2)
def defn(x,y,z,st,ct,so,co):
    return pow(st*(co*x-so*z),2)-2*ct*st(co*x-so*z)*y+pow(ct*y,2)

