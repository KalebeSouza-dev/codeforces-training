t= int(input())
for _ in range(t):
    n = int(input())
    array = sorted([int(i) for i in input().split()], reverse= True)
    gold = 0
    if n %2 == 0:
        for i in range(0, n, 2):
            gold += max(array[i], array[i + 1])
    else:
        for i in range(0, n - 1, 2):
            gold += max(array[i], array[i + 1])
        gold += array[-1]
 
    print(gold)