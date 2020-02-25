N, M = map(int,input().split())
result = []

def getResult(n,inList):
    if n>=M:
        tmpList = [0]*M
        for i in range(M):
            tmpList[i] = inList[i]
        result.append(tmpList)
        return
    else:
        for i in range(1,N+1):
            inList[n] = i
            getResult(n+1,inList)
            inList[n] = 0

retList = [0]*M
getResult(0,retList)
for ret in result:
    print(*ret)