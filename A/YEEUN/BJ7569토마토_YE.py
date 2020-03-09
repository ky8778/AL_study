#토마토
from collections import deque
def BFS():
    while q:
        nowy, nowx, nowh, day = q.popleft()

        for h in range(3):
            nexth = nowh + dh[h]
            if 0<= nexth < H :
                if h == 0:
                    for d in range(4):
                        nexty = nowy + dy[d]
                        nextx = nowx + dx[d]
                        if 0<=nexty<N and 0<=nextx<M and not arr[nexth][nexty][nextx]:
                            arr[nexth][nexty][nextx] = 1
                            q.append((nexty, nextx, nexth, day+1))
                else:
                    if not arr[nexth][nowy][nowx]:
                        arr[nexth][nowy][nowx] = 1
                        q.append((nowy, nowx, nexth, day+1))
    return day

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
dh = [0, 1,-1]

q = deque()
for h in range(H):
    for y in range(N):
        for x in range(M):
            if arr[h][y][x] == 1:
                q.append((y, x, h, 0))

day = BFS()

for h in range(H):
    for y in range(N):
        for x in range(M):
            if arr[h][y][x]==0: day = -1

print(day)