while 1:
    try:
        s=input()
        n=[]
        for i in s:
            n.append(int(i))
        ans=n[0]+n[1]*9+n[2]*6+n[3]*4+n[4]*6+n[5]*6+n[6]*4+n[7]*6+n[8]*9+n[9]
        print(ans%10)
    except:break
    