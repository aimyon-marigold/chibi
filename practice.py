while True:
    try:
        n = int(input())
    except:
        break
    print(n * (n + 1) // 2 + 1)
    