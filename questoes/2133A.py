t = int(input())
for _ in range(t):
    n = int(input())
    array = set([int(i) for i in input().split()])
    if len(array) >= n:
        print("NO")
    if len(array) < n:
        print("YES")