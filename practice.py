while 1:
    b,r,g,c,s,t=map(int,input().split())
    if [b,r,g,c,s,t].count(0)==6:break
    print(100+(b+r)*15+g*7+c*2+(b*5+r*3)*13-(t-(s+b*5+r*3))*3)
    