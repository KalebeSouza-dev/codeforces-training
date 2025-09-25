t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    if (len(set(a)) + len(set(b))) < 4:
        print("NO")
    else:
        print("YES")