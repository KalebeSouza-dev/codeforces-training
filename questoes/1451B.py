t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    for _ in range(k):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        result = "NO"
        for i in range(l):
            if s[l] == s[i]:
                result = "YES"
                break
        if result == "NO":
            for j in range(r+1, n):
                if s[r] == s[j]:
                    result = "YES"
                    break
        print(result)