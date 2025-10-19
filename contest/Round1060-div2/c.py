from math import gcd
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    
    if len(set(a)) == 1 and a[0] == 1: 
        print(2)
        continue
    par = 0
    ss = set()
    for i in range(n):
        if a[i] > 1:
            if a[i] in ss:
                print(0)
                break
            else:
                ss.add(a[i])
        if a[i] % 2 == 0:
            par += 1
            if par == 2: 
                print(0)
                break
    else:
        f = False
        t1 = False
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if gcd(a[i] + 1, a[j]) > 1 or gcd(a[j] + 1, a[i]) > 1:
                    t1 = True
                if gcd(a[i], a[j]) > 1:
                    print(0)
                    f = True
                    break
            if f: break
        else:
            if t1: print(1)
            elif par == 1: print(1)
            else: print(2)
        