t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    a = []
    idx = 1
    for i in range(n):
        if i == 0:
            diff = b[i]
        else:
            diff = b[i] - b[i-1]
        
        if diff == i + 1:
            a.append(idx)
            idx += 1
        else:
            pos = i - diff
            a.append(a[pos])
    
    print(*a)