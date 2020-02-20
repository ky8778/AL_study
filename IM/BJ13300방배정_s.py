import math
N, K = map(int, input().split())
students = [[0]*6 for _ in range(2)]
cnt = 0

for N in range(N):
    S, Y = map(int, input().split())
    students[S][Y-1] += 1

for s in range(2):
    for y in range(6):
        if students[s][y] > K:
            cnt += (students[s][y] / K)
            cnt = math.ceil(cnt)
        elif 0 < students[s][y] <= K:
            cnt += 1
print(cnt)