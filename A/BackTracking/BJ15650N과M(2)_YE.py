#N과 M(2)
def select(start, temp):
    global M
    if len(temp)==M:
        tp=temp[:]
        alist.append(tp)
        return 
    else:
        for i in range(start, N):
            if visited[i]==False:
                visited[i]=True
                temp.append(tlist[i])

                select(i, temp)

                visited[i]=False
                temp.remove(tlist[i])

N, M = map(int, input().split())
tlist = [i for i in range(1,N+1)]
visited = [False]*N
alist=[]
temp=[]


select(0, temp)

for k in range(len(alist)):
    print(*alist[k])