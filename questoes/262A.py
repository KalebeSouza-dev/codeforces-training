n, k = map(int, input().split())
array = [list(i) for i in input().split()]
cont = 0
for i in range(n):
    if array[i].count('4') + array[i].count('7') <= k:
        cont += 1
print(cont)