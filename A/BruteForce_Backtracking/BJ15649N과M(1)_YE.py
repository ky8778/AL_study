def select(temp):
    global M
    if len(temp)==M:
        tp=temp[:]
        alist.append(tp)
        return
    else:
        for i in range(N):
            if visited[i]==False:
                visited[i]=True
                temp.append(tlist[i])

                select(temp)

                visited[i]=False
                temp.remove(tlist[i])
    

N, M = map(int, input().split())
tlist = [i for i in range(1,N+1)]
visited = [False]*N
alist=[]
temp=[]

select(temp)

for k in range(len(alist)):
    print(*alist[k])