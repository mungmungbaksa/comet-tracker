import math
def inclination(a,b):
    omega=math.atan(-((math.sqrt(1+(a*a)))/b))
    return omega
def longitude_of_ascending_node(a,b):
    i=math.atan(a)
    return i