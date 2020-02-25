N,M = map(int,input().split())
result = []
checkList = [False for _ in range(N+1)]

def getResult(n,inList):
    if n>=M:
        tmpList = [0]*M
        for i in range(M):
            tmpList[i] = inList[i]
        result.append(tmpList)
        return
    else:
        for i in range(1,N+1):
            if not checkList[i]:
                checkList[i] = True
                inList.append(i)
                getResult(n+1,inList)
                inList.pop()
                checkList[i] = False

retList = []
getResult(0,retList)
for row in result:
    for col in row:
        print(col,end=' ')
    print()