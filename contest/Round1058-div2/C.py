t = int(input())
for i in range(t):
    n = int(input())
    #print(bin(n)[2:])
    #print(bin(n)[2:][::-1])
    if n == 0: 
        print("YES")
        continue
    
    st = bin(n)[2:]
    st2 = bin(n)[2:][::-1]
    for i in range(len(st2)):
        if st2[i] == "1":
            st2 = st2[i:]
            break
    #print(st, st2, bin(int(st, 2) ^ int(st2, 2)))
    result = bin(int(st, 2) ^ int(st2, 2))[2:]
    if st2 == "1":
        print("NO")
    elif result == result[::-1]: 
        print("YES")
    else:
        print("NO")