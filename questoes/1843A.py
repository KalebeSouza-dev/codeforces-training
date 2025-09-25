t = int(input())
for i in range(t):
    n = int(input())
    array = sorted([int (i) for i in input().split()])
    if n == 1: print(0)
    else:
        mini = 0
        maxi = 0
        for i in range(n//2):
            mini += array[i]
        for i in range(len(array) - n//2, len(array)):
            maxi += array[i]
        print(maxi - mini)