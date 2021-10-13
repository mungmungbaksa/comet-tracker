from math import *
#d(거리,AU), 방위각(°), 고도(°)
def xobservation(d,alpha,beta): # x좌표 변환 모듈 (지구 공전궤도 반지름 포함)
    return 1+(d*cos(beta)*cos(alpha))
def yobservation(d,alpha,beta):# y좌표 변환 모듈
    return d*cos(beta)*sin(alpha)
def zobservation(d,alpha,beta): # z좌표 변환 모듈
    return d*sin(beta)