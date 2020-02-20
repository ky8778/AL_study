import sys
sys.stdin = open('IM 1번.txt', 'r')

cnt_square = []
square = []
cnt = 0
for i in range(4):
    points = list(map(int, input().split()))
    square.append(points)

for n in range(max(square[0][2], square[1][2], square[2][2], square[3][2]) + 1):
    cnt_square.append([])
    for m in range(max(square[0][3], square[1][3], square[2][3], square[3][3]) + 1):
        cnt_square[n].append(None)

for i in range(4):
    for j in range(square[i][0],square[i][2]):
        for k in range(square[i][1],square[i][3]):
            if cnt_square[j][k] == '*':
                continue
            else:
                cnt_square[j][k] = '*'
                cnt += 1

print(cnt)