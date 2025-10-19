n = int(input())
arr = sorted([int(i) for i in input().split()])
ml = mr = -1
for i in arr:
    if i <= 500000:
        ml = i
    if i > 500000:
        mr = i
        break
    
if mr != -1 and ml != -1:
    print(max(ml - 1, 1000000 - mr))
elif mr == -1:
    print(ml - 1)
else: 
    print(1000000 - mr)