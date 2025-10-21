t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == b: print(0)
    else:
        aa = bin(a)[2:]
        bb = bin(b)[2:]
        if len(bb) > len(aa):
            print(-1)
            continue
        obj = ['0'] * (max(len(aa) - len(bb), 0))   
        obj += list(bin(b)[2:])
        ini = ['0'] * (max(len(bb) - len(aa), 0))
        ini += list(bin(a)[2:])

        #print(ini, obj)

        out = []
        for i in range(len(obj) - 1, -1, -1):
            # print(obj[i], ini[i], i)
            if obj[i] == ini[i]: continue
            if obj[i] == '1' and ini[i] == '0':
                out.append(2 ** (len(obj) - 1 - i))
            elif obj[i] == '0' and ini[i] == '1':
                out.append(2 ** (len(obj) - 1 - i))
            # print(out)

        print(len(out))
        print(*out)