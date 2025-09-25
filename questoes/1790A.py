t = int(input())
for _ in range(t):
    pi = list("314159265358979323846264338327")
    n = list(input())
    c = 0

    for i in range(len(n)):
        if n[i] == pi[i]: c += 1
        else: break

    print(c)