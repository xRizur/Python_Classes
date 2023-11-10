while True:
    print("podaj liczbe, wpisz stop by zakonczyc")
    x = input()
    if x == 'stop':
        break
    if x.isdigit() == False:
        print("error, podaj liczbe")
        continue
    else:
        print(pow(int(x), 3))