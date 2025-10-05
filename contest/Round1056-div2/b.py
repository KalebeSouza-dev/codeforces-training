t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n * n - k == 1: print("NO")
    else:
        print("YES")
        if k >= n * n:
            linha = ["U"] * n
            for i in range(n):
                print("".join(linha))
        else:
            x = n * n - k
            for i in range(n):
                if i == 0:
                    if x >= n:
                        linha = ["L"] * n
                        linha[0] = "R"
                        print("".join(linha)) 
                        x -= n
                    elif x != 0:
                        linha = ["L"] * x 
                        linha[0] = "R"
                        for i in range(n - len(linha)):
                            linha.append("D")
                        print("".join(linha)) 
                        x = 0
                elif x == 0:
                    linha = ["D"] * n
                    print("".join(linha))
                else:
                    linha = []
                    for i in range(min(n, x)):
                        linha.append("U")
                    for i in range(n - len(linha)):
                        linha.append("D")
                    print("".join(linha)) 
                    x -= min(x, n)