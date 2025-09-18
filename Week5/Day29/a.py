n, m = map(int, input().split())
col = [[] for i in range(m)]
for i in range(n):
    array = [int(i) for i in input().split()]
    for i in range(m):
        col[i].append(array[i])

c = 0
for i in range(m):
    c += max(col[i])

print(c)
