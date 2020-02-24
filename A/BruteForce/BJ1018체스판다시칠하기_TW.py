import sys
sys.stdin = open('1018.txt','r')

def INTO_BIN(a) : # 체스판 정보를 W=1, B=0 으로 변경 // input 받을 때 map과 함께 사용
    if a == 'B' : return 0
    else : return 1


def CHECKER(r, c) :
    global min_cnt

    cnt1, cnt2 = 0, 0
    for i in range(8) :
        for j in range(8) :
            if B[r+i][c+j] != (i+j) & 1 : cnt1 += 1 # 0, 1, 0, 1 순서
            if B[r+i][c+j] != (i+j+1) & 1: cnt2 += 1 # 1, 0, 1, 0 순서

    if cnt1 < min_cnt: min_cnt = cnt1
    if cnt2 < min_cnt: min_cnt = cnt2


R, C = map(int, input().split())
B = [list(map(INTO_BIN, input())) for _ in range(R)]

min_cnt = 64

for r in range(R-7) :
    for c in range(C-7) :
        CHECKER(r, c)

print(min_cnt)