#단지번호 붙이기

def DFS(nowy, nowx):
    global count

    arr[nowy][nowx] = 2

    for d in range(4):
        nexty = nowy + dy[d]
        nextx = nowx + dx[d]
        if 0<=nexty<N and 0<=nextx<N and arr[nexty][nextx]==1:
            count+=1
            DFS(nexty, nextx)
    

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
dy = [1,-1,0,0]
dx = [0,0,1,-1]
anw = 0
anwlist = []

for y in range(N):
    for x in range(N):
        count = 1
        if arr[y][x] == 1 : 
            DFS(y,x)
            anw+=1
            anwlist.append(count)

print(anw)
anwlist.sort()
for t in anwlist:
    print(t)