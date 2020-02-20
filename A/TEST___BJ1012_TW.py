import sys
sys.stdin = open('1012.txt', 'r')

Dr = [1, -1, 0, 0]
Dc = [0, 0, -1, 1]

def GO(r, c) :
    Ground[r][c] = 0

    for i in range(4) :
        Nr = r + Dr[i]
        Nc = c + Dc[i]

        if 0 <= Nr < Row_n and 0 <= Nc < Col_n and Ground[Nr][Nc] :
                GO(Nr, Nc)


T = int(input())

for tc in range(1, T+1) :
    Col_n, Row_n, K = map(int, input().split())

    Ground = [[0] * Col_n for _ in range(Row_n)]

    for k in range(K) :
        c, r = map(int, input().split())
        Ground[r][c] = 1

    print(Row_n, Col_n)
    for r in Ground :
        print(r)
    print()


    cnt = 0

    for r in range(Row_n) :
        for c in range(Col_n) :
            if Ground[r][c] :
                cnt += 1
                GO(r, c)

    for r in Ground :
        print(r)
    print()

    print(cnt)