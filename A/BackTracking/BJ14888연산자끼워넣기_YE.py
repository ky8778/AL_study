#연산자 끼워넣기
def makeStack(): #연산자 조합 정하기
    global test, N
    if len(test)==N-1:
        tt=test[:]
        possible.append(tt)
        return

    for i in range(4):
        if tlist[i]:
            test.append(i)
            tlist[i]-=1

            makeStack()

            test.pop()
            tlist[i]+=1

def getResult(pre, next, operator):
    if operator%4==0:
        return pre+next
    elif operator%4==1:
        return pre-next
    elif operator%4==2:
        return pre*next
    else:
        if pre<0:
            pre*=-1
            return pre//next*-1
        else:
            return pre//next

N = int(input())
nlist = list(map(int, input().split())) #N개
tlist = list(map(int, input().split())) #N-1개 / + - * //
test = []
possible = []
maxn = -987654321
minn = 987654321

i = 0

makeStack()

n = 1
for temp in possible:
    result = nlist[0]
    while n<N:
        result = getResult(result, nlist[n], temp[n-1])
        n+=1

    if maxn<result:
        maxn=result
    if minn>result:
        minn=result
    n = 1

print(maxn)
print(minn)