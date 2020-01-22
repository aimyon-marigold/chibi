n = int(input())
m = int(input())
lst = [i + 1 for i in range(2 * n)]
for _ in range(m):
  k = int(input())
  if k == 0:
    lst1 = lst[0:n]
    lst2 = lst[n:2 * n]
    lst = [lst2[i//2] if i % 2 else lst1[i//2] for i in range(n * 2)]
  else:
    lst1 = lst[0:k]
    lst2 = lst[k:2 * n]
    lst = lst2 + lst1
for i in lst:
  print(i)
  