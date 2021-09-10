from math import *
#d=(AU),alpha=x->y,beta=xy->z
def xobservation(d,alpha,beta):
    return 1+(d*cos(beta)*cos(alpha))
def yobservation(d,alpha,beta):
    return d*cos(beta)*sin(alpha)
def zobservation(d,alpha,beta):
    return d*sin(beta)