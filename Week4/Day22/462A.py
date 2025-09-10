n = int(input().strip())
m = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        cont = 0
        
        if i != 0 and m[i-1][j] == "o":
            cont += 1
        if i < n -1 and m[i+1][j] == "o":
            cont += 1
        if j < n -1 and m[i][j+1] == "o":
            cont += 1
        if j != 0 and m[i][j-1] == "o":
            cont += 1
        
        if cont % 2 == 1:
            print("NO")
            exit(0)
else:
    print("YES")