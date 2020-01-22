n=int(input())
for i in range(n):
    runner=0
    out=0
    score=0
    while 1:
        state=input()
        if state=="HIT":
            if runner<3:
                runner+=1
            else:
                score+=1
        elif state=="HOMERUN":
            score+=runner+1
            runner=0
        else:
            out+=1
            if out==3:break
    print(score)
    