t = int(input())
for _ in range(t):
    n = int(input())
    array = [int(i) for i in input().split()]
    result = []
    for i in range(n):
        op = input().split()
        d = 0
        u = 0
        for s in op[1]:
            if s == "U": u += 1
            else: d += 1
        result.append((array[i] + d - u) % 10)
    print(*result)
        