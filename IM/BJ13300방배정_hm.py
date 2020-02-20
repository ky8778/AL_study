Data = [[0]*6 for _ in range(2)]

N, K = map(int, input().split())

for i in range(N):
    info = list(map(int, input().split()))
    Data[info[0]][info[1]-1] += 1

rst = 0

for i in range(2):
    for j in range(6):
        rst += Data[i][j]//K
        if Data[i][j]%K:
            rst +=1

print(rst)