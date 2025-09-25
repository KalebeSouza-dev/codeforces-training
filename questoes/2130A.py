t = int(input())
for _ in range(t):
    n = int(input())
    array = [int(i) for i in input().split()]
    s = sum(array)
    for i in range(n):
        if array[i] == 0: s += 1
    print(s)