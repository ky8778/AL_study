import sys
sys.stdin = open('1260.txt', 'r')

def DFS(now) :
    print(now, end=' ')
    Vstd[now] = 1

    for next in range(1001) :
        if MAP[now][next] and not Vstd[next] :
            DFS(next)

def BFS(start) :

    Q = [start]
    Vstd = [0] * 1001
    Vstd[start] = 1
    print(start, end=' ')

    while Q :
        for i in range(len(Q)) :
            n = Q.pop(0)
            for next in range(1001) :
                if MAP[n][next] and not Vstd[next] :
                    Q.append(next)
                    Vstd[next] = 1
                    print(next, end = ' ')





V, E, start = map(int,input().split())
MAP = [[0] * 1001 for _ in range(1001)]


for _ in range(E) :
    v1, v2 = map(int, input().split())
    MAP[v1][v2] = 1
    MAP[v2][v1] = 1

Vstd = [0] * 1001
DFS(start)
print()


BFS(start)