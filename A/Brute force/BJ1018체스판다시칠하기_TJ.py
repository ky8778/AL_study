N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]
chess1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]*4
chess2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]*4
min_cnt = 2500
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        cnt1 = 0
        cnt2 = 0
        for y in range(8):
            for x in range(8):
                if board[y+i][x+j] != chess1[y][x]:
                    cnt1 += 1
                if board[y+i][x+j] != chess2[y][x]:
                    cnt2 += 1
        if min_cnt > min(cnt1,cnt2):
            min_cnt = min(cnt1,cnt2)
print(min_cnt)
