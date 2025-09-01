t = int(input())

for _ in range(t):
    n = int(input())
    array = [int(i) for i in input().split()]
    r = []
    for i in array:
        if i != -1:
            r.append(i)
    if len(set(r)) == 1 and r[0] != 0:
        print("YES")
    elif len(set(r)) == 0:
        print("YES")
    else: 
        print("NO")
        