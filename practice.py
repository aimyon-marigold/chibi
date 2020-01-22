while True:
  b, r, g, c, s, t = map(int, input().split())
  if b + r + g + c + s + t == 0:
    break
  normal_game = t - b * 5  - r * 3
  bonus_game  = b * 5 + r * 3
  print(100 + bonus_game * 16 + 15 * b + 15 * r + 7 * g + 2 * c + 3 * s - t * 3)
  