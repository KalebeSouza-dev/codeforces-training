t = int(input())
for _ in range(t):
    n = int(input())
    flag = False
    for i in range(int(n**(0.5)) + 1):
        if flag == True: break
        for j in range(int(n**(0.5)) + 1):
            if (i + j) ** 2 == n:
                print(i, j)
                flag = True
                break
    if not flag:
        print(-1)