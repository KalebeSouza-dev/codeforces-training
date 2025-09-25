t = int(input())
for  _ in range(t):
    n, x = map(int, input().split())
    array = [int(i) for i in input().split()]
    ini = fim = 0
    for i in range(n):
        if array[i] == 1:
            ini = i
            break
    for i in range(n - 1, -1, -1):
        if array[i] == 1:
            fim = i
            break
        
    #print(ini, fim, x)
    if abs(fim - ini) < x:
        print("YES")
    else:
        print("NO")