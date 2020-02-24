#덩치

N =int(input())
tlist=[list(map(int, input().split())) for _ in range(N)]
nlist=[1]*N

for temp in range(N-1):
    for next in range(temp, N):
        tempx = tlist[temp][0]
        tempy = tlist[temp][1]
        nextx = tlist[next][0]
        nexty = tlist[next][1]

        if tempx>nextx and tempy>nexty:
            nlist[next]+=1
        if tempx<nextx and tempy<nexty:
            nlist[temp]+=1

print(*nlist)
    