#바이러스
import sys
sys.stdin = open('input.txt', 'r')

def BFS(start):
    queue = [start]
    visited = [start]
    
    while queue:
        now = queue.pop(0)
        for t in range(1,N+1):
            if graph[now][t]==1 and t not in visited:
                visited.append(t)
                queue.append(t)
    print(len(visited)-1)

N = int(input())
V = int(input())
tlist = [list(map(int, input().split())) for _ in range(V)]
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
#인접행렬 구하기
for i in range(V):
    graph[tlist[i][0]][tlist[i][1]] = 1
    graph[tlist[i][1]][tlist[i][0]] = 1

BFS(1)
