t= int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = input()
    if "1" not in arr:
        print(0)
        continue
    o = []
    for i in range(n):
        if arr[i] == "1":
            o.append(i + 1)
    
    out = 1
    for i in range(1, len(o)):
        if abs(o[i] - o[i - 1]) < k:
            continue
        out += 1
    print(out)




