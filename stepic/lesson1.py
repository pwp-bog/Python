password = bool(input("Введите пароль: "))

while password:
    print("Loh")
    password = input("Введите пароль: ")
    if password == "loh":
        print("End.")
        break
else:
    print("down")