n = input()
n = n.replace("#", "")
n = int(n)

for i in range(n):
    str = input()
    if "#" in str:
        index = str.index("#")
        changed_str = str.replace(str[index::], "")
        str = changed_str.rstrip()
        print(str)
    else:
        print(str)