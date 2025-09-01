from math import gcd
x, y, a, b = map(int, input().split())

aa = a // (gcd(a, b))
bb = b // (gcd(a, b))

a = x // aa
b = y // bb

print(min(a, b))