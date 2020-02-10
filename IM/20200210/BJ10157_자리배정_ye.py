#자리배정
C,R = map(int, input().split())
pnum=int(input())
arr=[[0 for _ in range(C)] for _ in range(R)]
if pnum>C*R:
    print(0)
else:
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    tempy=R-1
    tempx=0
    d=0
    i=1
    while i<pnum:
        arr[tempy][tempx]=-1
        nexty=tempy+dy[d]
        nextx=tempx+dx[d]
        if nexty<0 or nexty>R-1 or nextx<0 or nextx>C-1 or arr[nexty][nextx]==-1:
            d=(d+1)%4
        tempy+=dy[d]
        tempx+=dx[d]
        i+=1
    print(tempx+1, R-tempy)