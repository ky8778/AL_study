import sys
sys.stdin = open('5105.txt', 'r')


Dr = [1, -1, 0, 0]
Dc = [0, 0, -1, 1]

def DFS(r, c, d=0):
    global minn, found
    Vstd[r][c] = 1

    if found : return

    if B[r][c] == 3:
        minn = d
        found = True
        return

    for i in range(4):
        Nr = r + Dr[i]
        Nc = c + Dc[i]

        if 0 <= Nr < N and 0 <= Nc < N and not Vstd[Nr][Nc] and B[Nr][Nc] != 1:
            DFS(Nr, Nc, d + 1)
            Vstd[Nr][Nc] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    B = [list(map(int, input())) for _ in range(N)]
    Vstd = [[0] * N for _ in range(N)]
    found = False

    for r in range(N):
        for c in range(N):
            if B[r][c] == 2:
                Sr, Sc = r, c
                break

    minn = 999999
    DFS(Sr, Sc)
    if not found: minn = 1

    print(f'#{tc} {minn-1}')