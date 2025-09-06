x, y = map(int, input().split())

r = "Ciel"
c = "C"
if not (y >= 2 and (x * 100 + y * 10) >= 220):
    print("Hanako")
    exit()
while True:
    if y >= 2:
        if (x * 100 + y * 10) >= 220:
            
            if c == "C":
                if x >= 2:
                    x -= 2
                    y -= 2
                else:
                    y -= (220 - (x * 100)) // 10
                    x = 0
                c = "H"
                r = "Ciel"
            else:
                if y >= 22:
                    y -= 22
                elif y >= 12:
                    y -= 12
                    x -= 1
                else:
                    y -= 2
                    x -= 2
                r = "Hanako"
                c = "C"
        else: break
    else: break

print(r)