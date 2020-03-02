N, M = map(int, input().split())
Board = [list(input()) for _ in range(N)]
min_cnt = 987654321

chess1 = [['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B']]

chess2 = [['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W']]

for n in range(N-8+1):
    for m in range(M-8+1):    # 시작점은 Board[n][m]
        cnt1 = 0
        cnt2 = 0
        for i in range(n, n + 8):    # 시작점부터 가로 8열 세로 8행 확인하기
            for j in range(m, m + 8):
                if Board[i][j] != chess1[i-n][j-m]:
                    cnt1 += 1
                if Board[i][j] != chess2[i-n][j-m]:
                    cnt2 += 1
        if min_cnt > cnt1:
            min_cnt = cnt1
        if min_cnt > cnt2:
            min_cnt = cnt2
print(min_cnt)