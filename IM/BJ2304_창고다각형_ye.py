#창고 다각형

N= int(input())
tlist=[list(map(int, input().split())) for _ in range(N)]
tlist.sort()
maxx=0
maxh=0

for i in range(len(tlist)):
    if tlist[i][1]>maxh:
        maxh=tlist[i][1]
        maxx=i

area=0
k=0
d=1

while k+d<=maxx:
    temph=tlist[k][1]
    tempx=tlist[k][0]
    nexth=tlist[k+d][1]
    nextx=tlist[k+d][0]
    if temph<=nexth:
        area+=temph*(nextx-tempx)
        k+=d
        d=1
    else:d+=1

k=len(tlist)-1
d=1
while k-d>=maxx:
    temph=tlist[k][1]
    tempx=tlist[k][0]
    nexth = tlist[k-d][1]
    nextx = tlist[k-d][0]
    if temph<=nexth:
        area+=temph*(tempx-nextx)
        k-=d
        d=1
    else:d+=1

print(area+maxh)
