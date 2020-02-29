import sys
sys.stdin = open('2580.txt', 'r')

# 값이 0인 좌표 R_list, C_list에 저장
# 각 좌표별로 가능한 값을 Promising list로 반환
# Promising list의 값을 이용해 DFS
# if 다음 좌표의 Promising list = [] : return // 이전 좌표의 다음 promising 값을 try
# 마지막 좌표까지 채워질 경우, 모든 좌표값이 스도쿠 조건을 만족한다는 뜻이므로, print
# 출력은 1번만 되어야 하므로 flag = printed 를 이용, if printed : return


def PROMISING(r, c) :
    Check = [0] * 10
    Promising = []

    for k in range(9) :
        Check[B[r][k]] += 1

    for k in range(9) :
        Check[B[k][c]] += 1

    if r < 3 : nr = 0
    elif r < 6 : nr = 3
    else : nr = 6

    if c < 3 : nc = 0
    elif c < 6 : nc = 3
    else : nc = 6

    for i in range(3) :
        for j in range(3) :
            Check[B[nr+i][nc+j]] += 1

    for n in range(1, 10) :
        if Check[n] == 0 : Promising.append(n)

    return Promising


def DFS(now) :
    global printed
    if printed : return

    if now == len(R_list) :
        if not printed:
            for r in B:
                print(*r)
            printed = True
            return

        else : return

    r = R_list[now]
    c = C_list[now]

    promising = PROMISING(r, c)

    for n in promising :
            B[r][c] = n
            now += 1
            DFS(now)
            B[r][c] = 0
            now -= 1


B = [list(map(int, input().split())) for _ in range(9)]

R_list=[]
C_list=[]
for r in range(9):
    for c in range(9):
        if not B[r][c]:
            R_list.append(r)
            C_list.append(c)

printed = False
DFS(0)
