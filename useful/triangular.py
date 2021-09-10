import math
#rad
def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    if (x-(math.radians(90)))%(math.radians(180)):
        return math.tan(x)
    else:
        return math.inf
#no usage of asin/acos -> only needs atan
def atan(x):
    return math.atan(x)