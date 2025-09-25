t = int(input())
for i in range(t):
    n = int(input())
    array = [int(i) for i in input().split()]
    result = []
    for i in array:
        result.append(n + 1 - i)
    print(*result)