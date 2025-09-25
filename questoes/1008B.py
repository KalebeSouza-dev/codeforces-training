n = int(input())
atual = 0
result = "YES"
for i in range(n):
    a, b = map(int, input().split())
    if i == 0:
        atual = max(a, b)
    else:
        if max(a, b) <= atual:
            atual = max(a,b)
        else:
            if min(a,b) > atual:
                result = "NO"
            else:
                atual = min(a, b)
print(result)