import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        a[i] %= k
        if a[i] == 0:
            a[i] = k

    ord = sorted(range(n), key=lambda i: (-a[i], i))

    print(" ".join(str(i + 1) for i in ord))
