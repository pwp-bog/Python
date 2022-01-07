n = input().split()
n = [int(x) for x in n]

n.sort()
print(*n, sep=" ")

n.sort(reverse=True)
print(*n, sep=" ")
