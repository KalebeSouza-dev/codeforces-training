t, k = map(int, input().split())
s = set()
for i in range(t):
    l, r = map(int, input().split())
    for j in range(l, r+1):
        s.add(j)
result = set()
for i in range(1, k+1):
    if i not in s:
        result.add(i)
print(len(result))
print(*result)
