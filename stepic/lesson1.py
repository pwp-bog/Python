n = int(input())

list = []

for i in range(n):
    list.append(input())

find_string = input()

for i in list:
    if find_string.upper() in i.upper():
        print(i)
    else:
        continue