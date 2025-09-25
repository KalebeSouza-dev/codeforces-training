t = int(input())
for _ in range(t):
    n = int(input())
    cont = 0
    for i in range(1,n):
        for j in range(1, n):
            if i + j == n:
                cont += 1
    print(cont)