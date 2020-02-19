a = [[1,2,3],[2,3,4],[5,6,7]]
b = [[1,2,3],[2,3,4],[5,6,7]]
c = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            c[i][j] += a[i][k] * b[k][j] 

for i in range(0,3):
    for x in range(0,3):
        print(c[i][x],end=" ")
    print()
