cont = 0
for i in range(1, 6):
    linha = input().split()
    if "1" in linha:
        cont += abs(3 - i)
        c = linha.index("1") + 1
        cont += abs(3 - c)
print(cont)