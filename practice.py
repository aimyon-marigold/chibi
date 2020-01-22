while True:
	K = int(input())
	if K == 0: break
	print(sum(list(map(int, input().split())))//(K-1))
    