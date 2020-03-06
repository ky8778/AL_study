#DFS와 BFS
def DFS(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)

            temp = graph[now][:]
            temp.sort()
            temp.reverse()

            for i in temp:
                if i not in visited:
                    stack.append(i)

    print(*visited)

def BFS(start):
    visited =[]
    queue = [start]
    visited = [start]

    while queue:
        now = queue.pop(0)
        temp = graph[now][:]
        temp.sort()

        for i in temp:
            if i not in visited:
                visited.append(i)
                queue.append(i)

    print(*visited)

N ,M , V = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
graph = dict()

#인접리스트 만들기
for tt in range(M):
    for i in range(2):
        if arr[tt][i] not in graph:
            graph[arr[tt][i]] = [arr[tt][i-1]]
            continue
        else :
            graph[arr[tt][i]] += [arr[tt][i-1]]

DFS(V)
BFS(V)
