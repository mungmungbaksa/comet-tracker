import math
def inclination(a,b): #궤도평면의 식으로부터 궤도 경사각을 출력한다
    omega=math.atan(-((math.sqrt(1+(a*a)))/b))
    return omega
def longitude_of_ascending_node(a,b): #궤도평면의 식으로부터 승교점 경도를 출력한다
    i=math.atan(a)
    return i