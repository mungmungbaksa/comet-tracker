#ax+by+c=0,dx+ey+f=0
def simultanious(a,b,c,d,e,f):
    x=((b*f)-(c*e))/((a*e)-(b*d))
    y=((c*d)-(a*f))/((a*e)-(b*d))
    return [x,y]