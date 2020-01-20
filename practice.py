while(1):
    try:
        d = int(input())
    except:
        break

    s = 0
    w = d
    while d < 600:
        h = d * d
        s += h * w
        d += w
    print(s)
    