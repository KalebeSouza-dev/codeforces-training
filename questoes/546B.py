n = int(input())
arr = sorted([int(i) for i in input().split()])

out = 0
for i in range(1, n):
    if arr[i] <= arr[i - 1]:
        out += arr[i - 1] + 1 - arr[i]
        arr[i] = arr[i - 1] + 1

print(out)
