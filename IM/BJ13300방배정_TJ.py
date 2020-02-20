N, K = map(int,input().split())
cnt = [[0,0] for _ in range(6)]
for i in range(N):
    S, Y = map(int,input().split())
    cnt[Y-1][S] += 1

room_cnt = 0
for y in range(6):
    for x in range(2):
        if cnt[y][x] // K >= 0 and cnt[y][x] % K > 0:
            room_cnt += 1 + cnt[y][x]//K
        elif cnt[y][x] // K >= 0 and cnt[y][x] % K == 0:
            room_cnt += cnt[y][x]//K

print(room_cnt)