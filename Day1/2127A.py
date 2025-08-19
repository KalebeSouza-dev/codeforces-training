t = int(input())

def mex(a, b, c):
    s = {a, b, c}
    for i in range(4): 
        if i not in s:
            return i

for _ in range(t):
    n = int(input())
    array = [int(i) for i in input().split()]

    for i in range(n - 2):
        a, b, c = array[i], array[i+1], array[i+2]

        if a == -1:
            candidatos_a = [0, 1, 2, 3]
        else: candidatos_a = [a]

        if b == -1:
            candidatos_b = [0, 1, 2, 3]
        else: candidatos_b = [b]

        if c == -1:
            candidatos_c = [0, 1, 2, 3]
        else: candidatos_c = [c]

        flag = False  
        for x in candidatos_a:
            for y in candidatos_b:
                for z in candidatos_c:
                    if mex(x, y, z) == max(x, y, z) - min(x, y, z):
                        flag = True
                        break
                if flag: break
            if flag: break

        if not flag:
            print("NO")
            break
    else:
        print("YES")
        