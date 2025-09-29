from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = Counter(arr)

    if len(cnt) == 1:
        print("Yes")
    elif len(cnt) > 2:
        print("No")
    else:
        v1, v2 = cnt.values()
        if abs(v1 - v2) <= 1:
            print("Yes")
        else:
            print("No")
