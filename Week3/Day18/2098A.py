t = int(input())
for _ in range(t):
    s = sorted(map(int, list(input())))
    result = ""
    for i in range(1, 11):
        valor = min(x for x in s if x >= 10 - i)
        s.pop(s.index(valor))
        result += str(valor)
    print(result)
    
