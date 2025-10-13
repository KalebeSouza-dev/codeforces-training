t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    freq = [0] * 101
    for x in arr:
        freq[x] += 1

    mex = 0
    while freq[mex] > 0:
        freq[mex] -= 1
        mex += 1

    print(mex)
