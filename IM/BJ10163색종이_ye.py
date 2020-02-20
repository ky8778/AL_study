#색종이

N= int(input())
arr=[[0 for _ in range(101)] for _ in range(101)]
for n in range(1,N+1):
    x,y,W,H=map(int, input().split())

    for w in range(W):
        for h in range(H):
            arr[y+h][x+w]=n

anwlist=[]
for n in range(1,N+1):
    ncount=0
    for y in range(101):
        for x in range(101):
            if arr[y][x]==n:
                ncount+=1
    anwlist.append(ncount)

for k in anwlist:
    print(k)





