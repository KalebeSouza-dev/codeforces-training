t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    arr = [int(i) for i in input().split()]
    f = True

    for i in range(n - 1):
        need = max(0, arr[i+1] - k)
        m += arr[i] - need
        if m < 0:
            f = False
            break

    print("YES" if f else "NO")
