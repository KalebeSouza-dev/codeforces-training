t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    if s == s[::-1]:
        print(0)
        print()
    else:
        out = []
        for i in range(n):
            if s[i] == "1":
                out.append(i + 1)
        if not out:
            for i in range(n):
                if s[i] == "0":
                    out.append(i + 1)
  
        print(len(out))
        print(*out)