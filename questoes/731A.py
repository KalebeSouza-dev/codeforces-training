s = input()
atual = 'a'
cont = 0

for c in s:
    dist = abs(ord(c) - ord(atual))

    dist = min(dist, 26 - dist)
    cont += dist
    atual = c

print(cont)
