import math
while True:
  n = int(input())
  if n == -1:
    break
  x, y = 1, 0
  for _ in range(n - 1):
    angle = math.atan2(y, x) + math.pi / 2
    x += math.cos(angle)
    y += math.sin(angle)
  print(x, y)
  