while 1:
    try:
        num = list(input())
    except EOFError:
        break

    for _ in range(9):
        nextlist = []
        for i in range(len(num)-1):
            tmp = (int(num[i]) + int(num[i+1])) % 10
            nextlist.append(tmp)

        num = nextlist

    print(num[0])
    