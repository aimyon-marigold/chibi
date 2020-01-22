while True:
    try:
        W = float(input())
        if W <= 48:
            print("light fly")
        elif W <= 51:
            print("fly")
        elif W <= 54:
            print("bantam")
        elif W <= 57:
            print("feather")
        elif W <= 60:
            print("light")
        elif W <= 64:
            print("light welter")
        elif W <= 69:
            print("welter")
        elif W <= 75:
            print("light middle")
        elif W <= 81:
            print("middle")
        elif W <= 91:
            print("light heavy")
        else:
            print("heavy")
    except EOFError:
        break
    
    