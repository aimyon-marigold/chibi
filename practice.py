def put_class(n):
    if n <= 48:
      print("light fly")
    elif n <= 51:
      print("fly")
    elif n <= 54:
      print("bantam")
    elif n <= 57:
      print("feather")
    elif n <= 60:
      print("light")
    elif n <= 64:
      print("light welter")
    elif n <= 69:
      print("welter")
    elif n <= 75:
      print("light middle")
    elif n <= 81:
      print("middle")
    elif n <= 91:
      print("light heavy")
    else:
      print("heavy")
  
  while True:
    try:
      put_class(float(input()))
    except EOFError:
      break
  
    