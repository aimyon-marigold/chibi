a = [0 for i in range(101)]
while True:
  try:
    n = int(input())
    a[n] += 1
  except EOFError:
    break

m = 0
for i in range(1, 101):
  m = max(m, a[i])
for i in range(1, 101):
  if a[i] == m:
    print(i)
    