def select(temp):
    global M
    if len(temp)==M:
        tp=temp[:]
        alist.append(tp)
        return
    else:
        for i in range(N):             
            temp.append(tlist[i])
            select(temp)
            temp.pop()
    

N, M = map(int, input().split())
tlist = [i for i in range(1,N+1)]
visited = [False]*N
alist=[]
temp=[]

select(temp)

for k in range(len(alist)):
    print(*alist[k])