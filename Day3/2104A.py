n = int(input())
for _ in range(n):
    a, b, c = [int(i) for i in input().split()]
    if (a + b + c) % 3 == 0:
        if (a+c) >= 2*b:
            print("YES")
        else:
            print("NO")
    
    else: 
        print("NO")


