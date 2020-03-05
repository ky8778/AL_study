def DFS(graph, start):
    visited = []
    stack = []

    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for Next in range(N, -1, -1):
                if graph[node][Next] == 1:
                    stack.append(Next)
    
    return visited


def BFS(graph, start):
    visited = []
    queue = []

    queue.append(start)

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for Next in range(N + 1):
                if graph[node][Next] == 1:
                    queue.append(Next)
    
    return visited

N, M, V = map(int,input().split())
edge = [list(map(int,input().split())) for _ in range(M)]
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(M):
    graph[edge[i][0]][edge[i][1]] = graph[edge[i][1]][edge[i][0]] = 1


print(*DFS(graph, V))
print(*BFS(graph, V))