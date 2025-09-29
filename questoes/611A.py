a, b, c = input().split()

if c == "week":
    if 5<= int(a) <= 6:
        print(53)
    else:
        print(52)
else:
    if int(a) <= 29: 
        print(12)
    elif int(a) <= 30: print(11)
    else: print(7)