while True:
    try:
        _= int(input())
    except:
        break
    t= 0
    ans= []
    for v in sorted(list(map(int, input().split()))):
        t+= v
        ans.append(t)
    print(sum(ans))
    