t = int(input())

for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()

    if len(set(list(s))) == 1:
        print(0)
        continue

    f = False
    for x in range(1, n + 1):
        ok = True
        for i in range(x - 1, n, x):
            if s[i] != c:
                ok = False
                break
        if ok:
            print(1)
            print(x)
            f = True
            break

    if not f:
        print(2)
        print(n, n - 1)
