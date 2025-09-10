t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    m = [list(map(int, list(input())))  for _ in range(n)]


    r = []
    for i in range(0,n,k):
        l = []
        for j in range(0,n,k):
            l.append(m[i][j])
        r.append(l)
    for i in r:
        print("".join(map(str,i)))