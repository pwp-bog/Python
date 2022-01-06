#   Количество строк
first_find = int(input())

#   Список строк
list_string = []

#   Заполнение строк
for i in range(first_find):
    list_string.append(input())

#   Количество запросов
secondary_find = int(input())

#   Список запросов
list_find = []

#   Заполнение запросов
for i in range(secondary_find):
    list_find.append(input())

#   Объявление
count = 0
new_list = []

#   Сам цикл
for fir in list_string:
    count = 0
    for sec in list_find:
        #   Если совпадает запрос с строкой счётчик плюс 1
        if sec.lower() in fir.lower():
            count += 1

        '''
        Если счётчик равен размеру списка с запросами, то обнуление счётчика
        и добавление в  новый список
        '''
        if count == len(list_find):
            new_list.append(fir)
        else:
            continue


print(*new_list, sep="\n")