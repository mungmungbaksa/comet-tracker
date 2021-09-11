from useful import simulatiouseq
def orbitalplanea(x1,y1,z1,x2,y2,z2):
    a=simulatiouseq.simultaniousx(y1,z1,x1,y2,z2,x2)
    return a
def orbitalplaneb(x1,y1,z1,x2,y2,z2):
    b=simulatiouseq.simultaniousy(y1,z1,x1,y2,z2,x2)
    return b