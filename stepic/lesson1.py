n = int(input())

list = []

for i in range(n):
    str = input()

    if str not in list:
        list.append(str)
    else:
        continue


print(*list, sep="\n")