n, h = map(int, input().split())
array = [int(i) for i in input().split()]

l = n
for i in range(n):
    if array[i] > h:
        l += 1
print(l)