def main(n):
    if n == 0:
        return False
    ans = 0
    for _ in range(int(n/4)):
        ans += int(input())
    print(ans)
    return True

while main(int(input())):
    pass
