def get_input():
    while True:
        try:
            yield ''.join(input())
        except EOFError:
            break

N = list(get_input())
for l in range(len(N)):
    cards = [1 for i in range(11)]
    cards[0] = 0
    C1,C2,C3 = [int(i) for i in N[l].split()]
    cards[C1] = 0
    cards[C2] = 0
    cards[C3] = 0

    point = C1+C2
    ok = 0
    ng = 0

    for i in range(1,11):
        if cards[i] == 1 and C1+C2+i <= 20:
            ok += 1
        elif cards[i] == 1:
            ng += 1

    if ok >= ng:
        print("YES")
    else:
        print("NO")
