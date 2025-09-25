t = int(input())
for _ in range(t):
    s = list(input())
    s.reverse()
    for i in range(len(s)):
        if  s[i] == "p": s[i] = "q"
        elif s[i] == "q": s[i] = "p"
    print("".join(s))