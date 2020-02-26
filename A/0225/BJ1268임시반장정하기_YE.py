#임시반장 정하기

def select():
    for i in range(N-1):
        for j in range(i+1, N):
            #print('main={}, compare={}'.format(i,j))
            main = arr[i]
            if countlist[i][j]!=0:
                continue
            else: compare = arr[j]

            for k in range(5):
                if main[k]==compare[k]:
                    countlist[i][j]=k+1
                    countlist[j][i]=k+1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
countlist=[[0 for _ in range(N)] for _ in range(N)]

select()
maxidx=maxn=0

#print(countlist)
for anw in range(len(countlist)):
    count=0
    for i in range(N):
        if countlist[anw][i]!=0:
            count+=1
    if maxn<count:
        maxidx=anw
        maxn=count

print(maxidx+1)