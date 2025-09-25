t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())
    result = [y]
    diff = 1
    for i in range(n - 1):
        result.append(result[-1] - diff)
        diff += 1
    result.reverse()
    if result[0] < x:
        print(-1)
    else:
        result[0] = x
        print(*result)
