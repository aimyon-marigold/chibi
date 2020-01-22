while True:
  r, c = map(int, input().split())
  if r == 0:
    break
  print(["yes", "no"][c % 2 and r % 2])
  