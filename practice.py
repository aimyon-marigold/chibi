while 1:
    try:s=input()
    except:break
    i,a,n=0,'',1
    for i in s:
        if n==0:n=int(i)
        elif i=='@': n=0
        else:
            a+=i*n
            n=1
    print(a)
    