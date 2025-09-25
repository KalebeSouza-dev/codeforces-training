n = int(input())
array = [int(i) for i in input().split()]
media = sum(array) // (n // 2)

dic = dict()
for i in range(n):
    # print(dic)
    # print(abs(media - array[i]))
    if abs(media - array[i]) not in dic.keys():
        dic[array[i]] = i
    else:
        print(dic[abs(media - array[i])] + 1, i + 1)
        del dic[abs(media - array[i])]
