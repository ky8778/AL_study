import sys
sys.stdin = open('input.txt', 'r')

def DFS(i, count):
    global anw
    if count == len(zeroidx):
        for tt in arr:
            print(*tt)
        anw = True
        return

    # while i <= len(zeroidx):
    temp = zeroidx[i]
    nowy = temp[0]
    nowx = temp[1]
    candidate = getNum(nowy, nowx)
    visited2 = [False for _ in range(len(candidate))]
    if not candidate:
        return

    for candi in range(len(candidate)):
        arr[nowy][nowx] = candidate[candi]
        visited2[candi] =  True
        DFS(i+1, count+1)
        arr[nowy][nowx] = 0
        visited2[candi] =  False
        if anw:
            break

def getNum(nowy, nowx):
    visited = [False for _ in range(10)]
    #가로 세로
    for y in range(9):
        for x in range(9):
            if arr[nowy][x]:
                visited[arr[nowy][x]] = True
        if arr[y][nowx]:
            visited[arr[y][nowx]] = True

    #어느 박스에 속했는지 찾기      
    boxy = boxx = 0
    for y in [3,6,9]:
        if nowy<y: boxy = y-3 ; break
    for x in [3,6,9]:
        if nowx<x: boxx = x-3 ; break

    for j in range(3):
        for i in range(3):
            if arr[boxy+j][boxx+i]:
                visited[arr[boxy+j][boxx+i]] = True
    candidate = []
    for tt in range(1,10):
        if not visited[tt]:
            candidate.append(tt)
    return candidate

arr = [list(map(int, input().split())) for _ in range(9)]
zeroidx = []
anw = False

for y in range(9):
    for x in range(9):
        if arr[y][x]==0:
            zeroidx.append([y,x])

DFS(0,0)

