t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = []

    for i in range(n):
        result.extend([int(i) for i in input().split()])
    if n == 1 and m == 1:
        print(-1)
    else:
        result.insert(0, result[-1])
        result.pop()
        for i in range(0, len(result), m):
            print(*result[i:i+m])
    
