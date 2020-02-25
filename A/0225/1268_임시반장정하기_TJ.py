def Class_president(max_cnt):
    for z in range(N):
        for y in range(N):
            C = 0
            for x in range(5):
                if z != y and Class[z][x] == Class[y][x]:
                    C += 1
            if C != 0:
                cnt[z] += 1

    for z in range(N):
        if max_cnt < cnt[z]:
            max_cnt = cnt[z]
            max_idx = z + 1

    return max_idx


N = int(input())
Class = [list(map(int,input().split())) for _ in range(N)]
cnt = [5] * N
print(Class_president(-1))



