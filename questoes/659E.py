import sys
sys.setrecursionlimit(200000)

n, m = map(int, input().split())

grafo = [[] for i in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    grafo[u].append(v)
    grafo[v].append(u)

visitados = [False] * (n + 1)

def dfs(u, parent):
    visitados[u] = True
    for v in grafo[u]:
        if not visitados[v]:
            if dfs(v, u):
                return True
        elif v != parent:
            return True
    return False

ans = 0

for i in range(1, n + 1):
    if not visitados[i]:
        ciclo = dfs(i, -1)
        if not ciclo:
            ans += 1

print(ans)