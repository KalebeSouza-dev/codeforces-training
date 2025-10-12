t = int(input())
for _ in range(t):
    n = int(input())
    tem = [False] * (2 * n + 1)
    arr = [int(i) for i in input().split()]
    conj = set(arr)

    falta = []
    for i in range(1, 2 * n + 1):
        if i not in conj: falta.append(i)
        else: tem[i] = True
    
    out = []
    for i in range(n):
        out.append(arr[i])
        for j in range(arr[i], 2 * n + 1):
            if tem[j] == False:
                out.append(j)
                tem[j] = True
                break
        else:
            print(-1)
            break
    else: 
        print(*out)