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
        cnt = 0
        for i in range(n, n + 8):    # 시작점부터 가로 8열 세로 8행 확인하기
            for j in range(m, m + 8):
                if Board[n][m] == 'B':
                    if Board[i][j] != chess1[i-n][i-m]:
                        cnt += 1
                else:
                    if Board[i][j] != chess2[i-n][i-m]:
                        cnt += 1
        if min_cnt > cnt:
            min_cnt = cnt
print(min_cnt)


# N, M = map(int, input().split())
# Board = [list(input()) for _ in range(N)]
# min_cnt = 987654321
#
# for n in range(N-8+1):
#     for m in range(M-8+1):
#         cnt = 0
#         if Board[n][m] == 'W':
#             for i in range(n, n + 8):
#                 for j in range(m, m + 8):
#                     if i % 2:
#                         if j % 2 and Board[i][j] == 'B':
#                             cnt += 1
#                         elif Board[i][j] == 'W':
#                             cnt += 1
#                     else:
#                         if j % 2 and Board[i][j] == 'W':
#                             cnt += 1
#                         elif Board[i][j] == 'B':
#                             cnt += 1
#         if Board[n][m] == 'B':
#             for i in range(n, n + 8):
#                 for j in range(m, m + 8):
#                     if i % 2:
#                         if j % 2 and Board[i][j] == 'W':
#                             cnt += 1
#                         elif Board[i][j] == 'B':
#                             cnt += 1
#                     else:
#                         if j % 2 and Board[i][j] == 'B':
#                             cnt += 1
#                         elif Board[i][j] == 'W':
#                             cnt += 1
#
#         if min_cnt > cnt:
#             min_cnt = cnt
# print(min_cnt)