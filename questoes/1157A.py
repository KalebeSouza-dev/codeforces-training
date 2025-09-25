n = int(input())
def remove0():
    while n % 10 == 0:
        n = n // 10
out = {n}

while True:
    x = len(out)
    n += 1
    while n % 10 == 0:
        n = n // 10
    out.add(n)
    if x == len(out): break

print(len(out))
