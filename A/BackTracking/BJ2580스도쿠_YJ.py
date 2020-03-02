from collections import deque

def Sudoku():
    global q
    if not q: return
    y, x = q.popleft()
    i = j = 0
    while not (i <= y < i+3): i += 3
    while not (j <= x < j+3): j += 3

    for k in range(1, 10):
        TF = False
        for n in range(i, i+3):
            for m in range(j, j+3):
                if field[n][m] == k:
                    TF = True
                    break
            if TF: break
        if TF: continue
        
        TF = False
        for idx in range(9):
            if field[y][idx] == k:
                TF = True
                break
            if field[idx][x] == k:
                TF = True
                break
        if TF: continue

        field[y][x] = k
        if not Sudoku():
            if not q: return
            field[y][x] = 0
    else:
        if field[y][x]: return True
        q.appendleft((y,x))
        return False

field = [[i for i in list(map(int, input().split()))] for j in range(9)]
q = deque()

for i in range(9):
    for j in range(9):
        if field[i][j] == 0:
            q.append((i,j))
while q:
    Sudoku()

for _ in range(len(field)):
    print(*field[_])