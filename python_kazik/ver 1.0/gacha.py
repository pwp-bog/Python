import random

#  Работа с балансом
balance = 0.0
print("Введите значение баланса: ")
balance = float(input())


#  Ставка


while(True):
    S = list(range(37))
    sRandom = random.choice(S)

    vvod = input("Загадайте и введите значение Красное, Чёрное или Зелёное: ")

    summStav = 99999999

    while(summStav > balance):
        summStav = 0.0
        print("Введите сумму ставки: ")
        summStav = float(input())
        if(summStav > balance):
            print("Ошибка, ставка не может превышать значение баланса... ")
        balance -= summStav

    if((sRandom == 36) and (vvod == "Зелёный")):  # Зелёный
        summStav *= 14
        balance += summStav
        print("Вы угадали, ваша ставка увеличилась в 14 раза")

    if((sRandom % 2 == 0) and (vvod == "Красный")):
        summStav *= 2
        balance += summStav
        print("Вы угадали, ваша ставка увеличилась в 2 раза")

    if((sRandom % 2 != 0) and (vvod == "Чёрный")):
        summStav *= 2
        balance += summStav
        print("Вы угадали, ваша ставка увеличилась в 2 раза")

    print("\tВаш баланс равен: ", balance)
