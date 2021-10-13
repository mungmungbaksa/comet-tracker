from useful import simulatiouseq # x+ay+bz=0의 형태
def orbitalplanea(x1,y1,z1,x2,y2,z2):
    a=simulatiouseq.simultaniousx(y1,z1,x1,y2,z2,x2)
    return a
def orbitalplaneb(x1,y1,z1,x2,y2,z2):
    b=simulatiouseq.simultaniousy(y1,z1,x1,y2,z2,x2)
    return b