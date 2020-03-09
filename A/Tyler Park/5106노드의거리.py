import sys
sys.stdin = open('5106.txt', 'r')

T = int(input())


def DFS(now, d=0):
    global found, m
    Vstd[now] = 1

    if d > m :
        return

    if now == Goal:
        if d < m : m = d
        found = True
        return

    for next in range(1, V+1):
        if MAP[now][next] and Vstd[next] == 0:

            DFS(next, d + 1)
            Vstd[next] = 0


for tc in range(1, T + 1):


    V, E = map(int, input().split())

    MAP = [[0] * (V + 1) for _ in range(V + 1)]
    Vstd = [0] * (V + 1)

    for e in range(E):
        v1, v2 = map(int, input().split())
        MAP[v1][v2] = 1
        MAP[v2][v1] = 1

    Start, Goal = map(int, input().split())
    found = False


    m = 99999
    DFS(Start)
    if not found: m = 0

    print(f'#{tc} {m}')