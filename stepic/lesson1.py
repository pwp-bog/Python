value_for_start_number2 = int(input())
value_max_dell = 0
for i in range(1, value_for_start_number2 + 1):  # Перебор числа в нужных границах
    for j in range(1, value_for_start_number2 + 1):  # Проверка на деление числа на делители
        # Если первое число делится на число из проверки на цело, то выполняем следующий код:
        if i % j == 0:
            value_max_dell += 1
    print(i, "+" * value_max_dell, sep="")
    value_max_dell = 0
