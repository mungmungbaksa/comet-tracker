import math
def sqrt(x):
    if x>=0:
        return math.sqrt(x)
    else:
        return complex(0,math.sqrt(-x))