h, m = map(int, input().split(":"))
x = f"{h:02}{m:02}"
cont = 0
if x == x[::-1]:
        print(cont)
else:
    while True:
        m += 1
        if m % 60 == 0:
            m = 0
            h += 1
            if h % 24 == 0:
                h = 0

        x = f"{h:02}{m:02}"
        cont += 1
        if x == x[::-1]:
            print(cont)
            break

