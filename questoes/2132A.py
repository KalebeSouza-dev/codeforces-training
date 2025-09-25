n = int(input())
for _ in range(n):
    n = int(input())
    a = list(input())
    x = int(input())
    b = list(input())
    c = input()
    
    inicio  = []
    final = []
    for i in range(x -1, -1, -1):
        if c[i] == "V":
            inicio.append(b[i])
        if c[i] == "D":
            final.insert(0, b[i])
    
    print(f'{"".join(inicio)}{"".join(a)}{"".join(final)}')