#토마토
from collections import deque

def BFS():
    while q:
        nowy, nowx, day = q.popleft()

        for d in range(4):
            nexty = nowy + dy[d]
            nextx = nowx + dx[d]
            if 0<=nexty<N and 0<=nextx<M and not arr[nexty][nextx] and not visited[nexty][nextx]:
                visited[nexty][nextx] = 1
                arr[nexty][nextx] = 1
                q.append((nexty, nextx, day+1))
    return day

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque()

for y in range(N):
    for x in range(M):
        if arr[y][x] == 1 and not visited[y][x]:
            visited[y][x] = 1
            q.append((y, x, 0))
day = BFS()

for y in range(N):
    for x in range(M):
        if arr[y][x]==0: day = -1

print(day)