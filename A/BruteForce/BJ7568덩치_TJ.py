N = int(input())
M = [list(map(int,input().split())) for _ in range(N)]

cnt = [1] * N

for i in range(N):
    for x in range(N):
        if i != x and M[i][0] < M[x][0] and M[i][1] < M[x][1]:
            cnt[i] += 1

print(*cnt)