t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    if (n  + b) % 2 == 0:
        if (b + a) % 2 == 0 or a <= b:
            print("YES")
        else:
            print("NO")
    else: 
        print("NO")