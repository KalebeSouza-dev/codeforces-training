n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    x = abs(x - 0)
    y = abs(y - 0)

    if x == y:
        print(x * 2)
    else:
        print(max(x, y) * 2 - 1)