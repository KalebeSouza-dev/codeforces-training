t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]

    cop = [arr[0]]
    for i in range(1, n):
        cop.append(max(arr[i], cop[-1]))

    out = 0

    if arr[0] >= arr[1]:
        out +=  1
        arr[0] = arr[1] - 1

    for i in range(1, n):
        if (i + 1) % 2 == 0:
            arr[i] = cop[i]
        if (i + 1) % 2 == 1 and arr[i] > arr[i - 1]:
            #print(arr[i], cop[i - 1])
            out += abs(arr[i] - cop[i - 1]) + 1
        elif (i + 1) % 2 == 1 and arr[i] == arr[i - 1]:
            #print(arr[i], cop[i - 1])
            out += 1
            arr[i] -= 1
    print(out)
        
