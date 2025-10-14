n = int(input())
impares = []
pares = []
for i in range(1, n+1):
    if i % 2 == 0: pares.append(i)
    else: impares.append(i)
out = []
out += pares
out += impares
out += pares

print(len(out))
print(*out)
