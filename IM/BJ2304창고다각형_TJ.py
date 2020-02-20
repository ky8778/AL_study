N = int(input())
L_H = []
for i in range(N):
    L, H = map(int,input().split())
    L_H.append([L, H])

L_H.sort()
max_H = 0
for i in range(N):
    if max_H < L_H[i][1]:
        max_L = L_H[i][0]
        max_H = L_H[i][1]
        max_idx = i

left_L = L_H[0][0]
left_H = L_H[0][1]
right_L = L_H[-1][0] + 1
right_H = L_H[-1][1]

result = 0
for i in range(N):
    if left_H < L_H[i][1]:
        result += (L_H[i][0] - left_L) * left_H
        left_L = L_H[i][0]
        left_H = L_H[i][1]
for i in range(N-1, -1, -1):
    if right_H < L_H[i][1]:
        result += (right_L - L_H[i][0] - 1)*right_H
        right_L = L_H[i][0] + 1
        right_H = L_H[i][1]
result += max_H*(right_L-left_L)
print(result)