def able(y,x):
    visited = [0] * 9
    for i in range(9):
        if sdoku[y][i]:
            visited[sdoku[y][i] - 1] = 1

    for i in range(9):
        if sdoku[i][x] and not visited[sdoku[i][x] - 1]:
            visited[sdoku[x][i] - 1] = 1

    for n in range(3):
        for m in range(3):
            if 3*n <= y < 3*(n + 1) and 3*m <= x < 3*(m + 1):
                for Y in range(3*n, 3*(n + 1)):
                    for X in range(3*m, 3*(m + 1)):
                        if sdoku[Y][X] and not visited[sdoku[Y][X] - 1]:
                            visited[sdoku[Y][X] - 1] = 1
    
    for k in range(9):
        if not visited[k]:
            reserve.append(k + 1)

def DFS(y,x,n):
    if n == 9:

    else:
        

    
sdoku = [list(map(int,input().split())) for _ in range(9)]
for y in range(9):
    for x in range(9):
        if sdoku[y][x] == 0:
            DFS(y,x,0)
 
for y in range(9):
    print(*sdoku[y])

