from math import inf

n = int(input())
for i in range(n):
    t = int(input())
    array = [int(i) for i in input().split()]
    soma = array[0]
    minimo = array[0]
    for i in range(1, t):
        minimo = min(minimo, array[i])
        soma += minimo
    print(soma)

