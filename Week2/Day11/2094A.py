n = int(input())
for i in range(n):
    s = input().split()
    saida = []
    for i in range(len(s)):
        saida.append(s[i][0])
    print("".join(saida))
