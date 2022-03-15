def mod(x,y,p):
    final=1
    x=x%p
    if x==0:
        return 0
    while y>0:
        if ((y&1)==1):
            final=(final*x)%p
        y=y>>1
        x=(x*x)%p
    return final

x,y,p=map(int,input().split())
print("Power is:",mod(x,y,p))
