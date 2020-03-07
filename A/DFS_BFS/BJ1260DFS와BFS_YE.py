
#DFS와 BFS
def DFS(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)

        for t in range(N,-1,-1):
            if graph[now][t] == 1 and t not in visited:
                stack.append(t)

    print(*visited)

def BFS(start):
    # visited =[]
    queue = [start]
    visited = [start]

    while queue:
        now = queue.pop(0)

        for t in range(N+1):
            if graph[now][t]==1 and t not in visited:
                visited.append(t)
                queue.append(t)

    print(*visited)

N ,M , V = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(M)]
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

#인접행렬 만들기
for x, y in arr:
    graph[x][y] = 1
    graph[y][x] = 1

DFS(V)
BFS(V)
