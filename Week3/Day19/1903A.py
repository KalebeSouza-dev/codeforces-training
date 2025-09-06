t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    array = [int(i) for i in input().split()]
    if array == sorted(array):
        print("YES")
    elif k > 1:
        print("YES")
    else:
        print("NO")