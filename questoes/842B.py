r, d = map(int, input().split())
n = int(input())
out = 0

for _ in range(n):
    x, y, s = map(int, input().split())
    dist2 = x * x + y * y
    if dist2 >= (r - d + s) ** 2 and dist2 <= (r - s) ** 2:
        out += 1

print(out)
