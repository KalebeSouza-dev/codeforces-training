from math import ceil

n, m, a, b = map(int, input().split())
if a * m <= b:
    print(a * n)
else:
    print(min((n // m) * b + a * (n % m), ceil(n / m) * b))