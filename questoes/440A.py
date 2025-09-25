n = int(input())
array = set([int(i) for i in input().split()])
for i in range(1, n + 1):
    if i not in array:
        print(i)
        break