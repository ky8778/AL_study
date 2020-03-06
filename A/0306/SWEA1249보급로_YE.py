#보급로
import sys
sys.stdin = open('input.txt', 'r')

def GO(tempy, tempx):
    global summ, N, minn
    stack = [(tempy, tempx)]
    sumstack = [arr[tempy][tempx]]
    visited[tempy][tempx] = 1
    nowy = nowx = 0

    while stack:
        nowy, nowx = stack.pop()
        summ = sumstack.pop()
        visited[nowy][nowx] = 1

        if nowy == N-1 and nowx == N-1:
            if summ <minn:
                minn = summ
            continue

        for d in range(4):
            nexty = nowy + dy[d]
            nextx = nowx + dx[d]
            if 0<=nexty<N and 0<=nextx<N and not visited[nexty][nextx]:
                stack.append([nexty, nextx])
                sumstack.append(summ+arr[nexty][nextx])

T = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    summ = 0
    minn = 987654321

    GO(0,0)

    print(f'#{tc+1} {summ}')