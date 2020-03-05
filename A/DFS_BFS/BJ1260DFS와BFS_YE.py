#DFS와 BFS
def DFS(start):
    visited = []
    stack = [start]

    while stack:
        if len(visited)==N:
            break
        now = stack.pop()

        if now not in visited:
            visited.append(now)
            temp = graph[now][:]
            temp.sort()
            temp.reverse()
            stack.extend(temp)
    print(*visited)

def BFS(start):
    visited =[]
    queue = [start]
    
    while queue:
        now = queue.pop(0)
        if now not in visited:
            visited.append(now)
            queue.extend(set(graph[now]) - set(visited))

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