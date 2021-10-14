import math
def semimajoraxis(d1,d2):
    v1=math.sqrt((2*132712440018900000000*(d1*d2+d2*d2))/d1) #단위: m/s
    epsilon=v1*v1*0.5-132712440018900000000/d1
    semi_major_axis=-132712440018900000000/(2*epsilon)
    return semi_major_axis/149597870700 #단위: AU