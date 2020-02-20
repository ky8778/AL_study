def issafe(y, x):
    if 0 <= y < R and 0 <= x < C:
        return False
    return True

def iszero(y,x):
    if P[y][x] != 0:
        return True
    return False


C, R = map(int, input().split())
num = int(input())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

P = [[0 for _ in range(C+1)]for _ in range(R+1)]

N = 1
y = 0
x = 0
i = 0

while C * R >= N:
    P[y][x] = N
    if N == num:
        print(x + 1,y + 1)
        break
    y += dy[i]
    x += dx[i]
    if issafe(y, x) or iszero(y,x):
        y -= dy[i]
        x -= dx[i]
        i = (i + 1)%4
        y += dy[i]
        x += dx[i]
    N += 1
if num > C * R:
    print(0)