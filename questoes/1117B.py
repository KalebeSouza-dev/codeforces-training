n, m, k = map(int, input().split())
array = sorted(list(map(int, input().split())))

max1 = array[-1]
max2 = array[-2]

blocos = m // (k + 1)
resto = m % (k + 1)

res = blocos * (max1 * k + max2) + resto * max1
print(res)
