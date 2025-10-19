s = input()
p = input()
t = int(input())
for _ in range(t):
    st = input()
    if "*" in p:
        print(12345)
        flag = True
        if len(st) < len(p) - 1:
            flag = False
            continue
        ini = fim = -1
        for i in range(len(p)):
            if p[i] == "*":
                ini = i
                fim = (len(st) - 1) - i
                break
        for j in range(ini):
            if p[i] == "?":
                if st[i] not in s:
                    flag = False
                    break
                if p[i] != st[i]:
                    flag = False
                    break
        for j in range(len(st) - 1, fim, -1):
            if p[i] == "?":
                if st[i] not in s:
                    flag = False
                    break
                if p[i] != st[i]:
                    flag = False
                    break
        if fim == ini: print("YES")
        else:
            for i in range(ini, fim + 1):
                if st[i] in s:
                    flag = False

        if not flag: print("NO")

    elif len(st) != len(p):
        print("NO")
    else:
        for i in range(len(p)):
            if p[i] == "?": 
                if st[i] not in s:
                    print("NO")
                    break
            else:
                if  p[i] != st[i]:
                    print("NO")
                    break
        else: print("YES")