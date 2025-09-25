t = int(input())
for i in range(1, t + 1):
    if (i * (i + 1)) / 2 == t:
        print("YES")
        break
else:
    print("NO")
    