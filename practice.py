while 1:
    a,b=input().split()
    if a=='0':break
    h=0
    for i,j in zip(a,b):h+=i==j
    print(h,len(set(a)&set(b))-h)
    