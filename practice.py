while True:
	try:
		n=int(input())
	except:
		exit()
	a=list(map(int,input().split()))
	a.sort()
	for i in range(n-1):
		a[i+1]+=a[i]
	print(sum(a))
    