t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    array = sorted([int(i) for i in input().split()])
    cont = 0
    coin = 0
    # print(array)
    for i in range(n - 1, -1, -1):
        # print(array[i])
        if array[i] > c:
            coin += 1
        else:
            array[i] *= 2**cont
            if array[i] > c:
                coin += 1
                cont -= 1
            cont += 1
        # print("coin", coin)
    print(coin)


