t = int(input())
for _ in range(t):
    a, b, x, y = map(int, input().split())
    print(max(abs(x - 1), abs(x - a)) + max(abs(y - 1), abs(y - b)))