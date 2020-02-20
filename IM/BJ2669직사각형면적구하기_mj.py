#직사각형 네 개의 합집합의 면적 구하기

import sys
sys.stdin = open('input.txt', 'r')

matrix = [list(map(int, input().split())) for i in range(4)]
#inMap = 범위 110으로 하면 거의 모든 범위 커버할 수 있음.

#최대 x값
lst = [] #두번째 x값 리스트
for i in range(4):
    lst.append(matrix[i][2])
max_x_range = max(lst)
#최대 y값
lst_a = [] #두번째 y값 리스트
for i in range(4):
    lst_a.append(matrix[i][3])
max_y_range = max(lst_a)
#최소 x값
lst_b = [] #첫번째 x값 리스트
for i in range(4):
    lst_b.append(matrix[i][0])
min_x_range = min(lst_b)
#최소 y값
lst_c=[] #첫번째 y값 리스트
for i in range(4):
    lst_c.append(matrix[i][1])
min_y_range = min(lst_c)

# for b in range(max_x_range):
#     for c in range(max_y_range):

matrix_b = []
count = 0
for i in range(max_y_range - min_y_range): # 0으로 채워진 8X7 매트릭스
    matrix_b.append([0 for j in range(max_x_range - min_x_range)])
# 1번 사각형을 보고 여기에 좌표가 속하면 matrix_b에서의 그 좌표값을 1로
# 1갯수

for idy in range(min_y_range,max_y_range):
    for idx in range(min_x_range,max_x_range):
        for i in range(4):
            if (matrix[i][0] <= idx < matrix[i][2]) and (matrix[i][1] <= idy < matrix[i][3]):
        #(첫번째 사각형 x 좌표 중 작은거 < idx < 첫번째 사각형 x 좌표 중 큰거) and (첫번째 사각형 y 좌표 중 작은거 < idy < 첫번째 사각형 y 좌표 중 큰거):
                matrix_b[idy-min_y_range][idx-min_x_range] = 1 #1로 채워줌
for i in range(max_y_range - min_y_range):
    for j in range(max_x_range - min_x_range):
        if matrix_b[i][j] == 1:
            count +=1
print(matrix_b)
print(count)

# for i in range(4):
#     matrix[0][i]
# if min_y_range<matrix[i][1]: # min y값과 비교해서 크면 matrix_b에 1채워넣기
#     matrix_b[i][1] = 1
# if max_y_range>matrix[i][3]:
#     matrix_b[i][1] = 1
#     if matrix_b[i][1] = 1: #이미 1이 채워져있어도 1 넣기



   

