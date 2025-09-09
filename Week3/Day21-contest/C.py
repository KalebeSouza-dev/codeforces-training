t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    divsB = []
    m = -1
    if b % 2 == 0:
        if (a + b) % 2 == 0:
            m = (a + b)
        for i in range(2, int(b**0.5) + 1, 2):
            if b % i == 0:
                if (b // i + a * i) % 2 == 0:
                    # print(a * i, b // i)
                    m = max(m, b // i + a * i)

                if i != b // i:
                    if (b // (b // i) + a * (b // i)) % 2 == 0:
                        m = max(m, b // (b // i) + a * (b // i))
                        # print("k", a * i, b // i)
                break
        print(m)
    else:
        if a % 2 == 1:
            for i in range(1, int(b**0.5) + 1, 2):
                if b % i == 0:
                    if (b // i + a * i) % 2 == 0:
                        m = max(m, b // i + a * i)

                    if i != b // i:
                        if (b // (b // i) + a * (b // i)) % 2 == 0:
                            m = max(m, b // (b // i) + a * (b // i))
                break
            print(m)

        else:
            print(-1)
                    