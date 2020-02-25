N,M = map(int,input().split())
result = []
checkList = [False] * (N+1)

def getResult(n,prev,inList):
    if n>=M:
        tmpList = [0] * M
        for i in range(M):
            tmpList[i] = retList[i]
        result.append(tmpList)
        return
    else:
        for i in range(prev+1,N+1):
            if not checkList[i]:
                checkList[i] = True
                inList[n] = i
                getResult(n+1,i,inList)
                checkList[i] = False
                inList[n] = 0
                    
retList = [0]*M
getResult(0,0,retList)
for ret in result:
    print(*ret)