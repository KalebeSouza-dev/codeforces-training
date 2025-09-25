x, y, s = map(int, input().split())
if x % s == 0 or y % s == 0:
    total = x//s + y//s
    print(total, 0)
else:
    total = (x + y) // s
    resto = s - max(x % s, y % s)
    if x % s +  y % s < s:
        resto = 0
    print(total, resto)