def f(n,x):
    for i in range(9):
        if n[i] != -1 and n[i] != x[i]: return 1
import itertools
u=[1,2,3,4,5,6,7,8,9]
a=0
n=list(map(int,input().split()))
for x in itertools.permutations(u):
    if f(n,x):continue
    if x[0]+x[2]+x[5]-x[8]+(x[1]+x[4]-x[7])*10+(x[3]-x[6])*100==0:a+=1
print(a)
