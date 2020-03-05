def DFS(y,x):
    visited = [0] * 9
    for n in range(3):
        for m in range(3):
            if n*3 <= y < (n + 1)*3 and m*3 <= x < (m + 1)*3:
                area_idx = n * 3 + m

    for i in range(9):
        if sdoku[y][i]:
            visited[sdoku[y][i] -1] = 1
        if sdoku_v[x][i]:
            visited[sdoku_v[x][i] - 1] = 1
        if sdoku_area[area_idx][i]:
            visited[sdoku_area[area_idx][i] - 1] = 1
    
    for j in range(9):
        if visited[j] == 0:
            sdoku[y][x] = j + 1
            sdoku_v[x][y] = j + 1
            

sdoku = [list(map(int,input().split())) for _ in range(9)]
sdoku_v = [[sdoku[y][x] for y in range(9)] for x in range(9)]
sdoku_area = [[0 for _ in range(9)]for _ in range(9)]
Y = 0
for y in range(3):
    for x in range(3):
        X = 0
        for n in range(3):
            for m in range(3):
                sdoku_area[Y][X] = sdoku[n + 3*y][m + 3*x]
                X += 1
        Y += 1

number = [n for n in range(1, 10)]
for y in range(9):
    for x in range(9):
        if sdoku[y][x] == 0:
            DFS(y,x)

for y in range(9):
    print(*sdoku[y])