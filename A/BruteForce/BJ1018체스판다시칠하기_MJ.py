N, M = map(int, input().split())
mat = [list(input()) for _ in range(N)] #MxN
cnt_lst = []
def check_difference(mat_88):
    compare_lst = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
    count = 0
    for i in range(8):
        for j in range(8):
            if mat_88[i][j] != compare_lst[i][j]:
                count += 1
    cnt_lst.append(min(64 - count, count))

for i in range(N-8+1):
    for j in range(M-8+1):
        mat_88 = []
        for k in range(8):
            mat_88.append(mat[i+k][j:j+8]) #8x8 매트릭스 조사
        check_difference(mat_88)
print(min(cnt_lst))

