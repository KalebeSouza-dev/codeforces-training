t = int(input())
for _ in range(t):
    n = int(input())
    c2 = c3 = c5 = 0
    
    while n % 2 == 0:
        n //= 2
        c2 += 1
    while n % 3 == 0:
        n //= 3
        c3 += 1
    while n % 5 == 0:
        n //= 5
        c5 += 1
    
    if n != 1:
        print(-1)
    else:
        print(c2 + 2*c3 + 3*c5)
