while True:
  try:
    c1, c2, c3 = map(int, input().split())
    lst = [i for i in range(1,11) if i not in (c1, c2, c3) and i + c1 + c2 <= 20]
    if len(lst) >= 4:
      print("YES")
    else:
      print("NO")

  except EOFError:
    break
