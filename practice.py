high_max=0
high_low=1000000
while True:
    try:
        N=float(input())
        if N>high_max:high_max=N
        elif N<high_low:high_low=N
    except:
        ans=high_max-high_low
        print("{:.1f}".format(ans))
        break
    
    