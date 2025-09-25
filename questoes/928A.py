s = list(input().lower())
for i in range(len(s)):
    if s[i] in "0oO": s[i] = "0"
    if s[i] in "1lLiI": s[i] = "1"
t = int(input())


for _ in range(t):
    k = list(input().lower())
    for i in range(len(k)):
        if k[i] in "0oO": k[i] = "0"
        if k[i] in "1lLiI": k[i] = "1"

    if k == s: 
        print("NO")
        break

else: print("YES")
