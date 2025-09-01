n = int(input())
for i in range(n):
    m, a, b, c = map(int, input().split())
    cont = 0
    if a >= m:
        cont += m
    else:
        cont += a
        if m - a >= c:
            cont += c
            c = 0
        else:
            c -= (m - a)
            cont += (m - a)
    if b >= m:
        cont += m
    else:
        cont += b
        if m - b >= c:
            cont += c
            c = 0
        else:
            c -= (m - b)
            cont += (m - b)
    print(cont)
    