while True:
  try:
    s, w, h = input().split(",")
    if float(w) / float(h) ** 2 >= 25:
      print(s)

  except EOFError:
    break
