t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    array = input().split()
    caminhada = 0
    cont= 0
    flag = False
    for num in array:
        if flag: 
            flag = False
            continue
        if num == "0":
            cont += 1
            if cont == k: 
                caminhada += 1
                cont = 0
                flag = True
        if num == "1":
            cont = 0
    print(caminhada)