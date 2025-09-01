n = int(input())
for i in range(n):
    s = input()
    lst = list(s)

    result = lst.count("T") * ["T"]
    for i in range(len(lst)):
        if lst[i] != "T":
            result.append(lst[i])
    print("".join(result))
