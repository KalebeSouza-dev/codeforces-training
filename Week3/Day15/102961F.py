n = int(input())
filmes = []
for _ in range(n):
    filmes.append(tuple(map(int, input().split())))

ordem = sorted(filmes, key=lambda x: x[1])

cont = 0
atual = 0
for inicio, fim in ordem:
    if inicio >= atual:
        cont += 1
        atual = fim
print(cont)
