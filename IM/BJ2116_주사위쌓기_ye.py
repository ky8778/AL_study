
import sys
sys.stdin=open('input.txt','r')

def selectmax(top, bottom):
    if (top==6 and bottom==5) or (top==5 and bottom==6):
        m=4
    elif top==6 or bottom==6:
        m=5
    else: m=6
    return m

def select(N,maxn):
    for bg in range(6):
        n=0
        top=arr[n][bg]
        if bg&1:
            s=selectmax(top, arr[0][bg-1])
        else:
            s=selectmax(top, arr[0][bg+1])

        n=1
        while n<N:
            dice = arr[n]
            for st in range(6):
                if dice[st]==top:
                    if st&1:
                        nexttop=dice[st-1]
                    else:
                        nexttop=dice[st+1]
                    s+=selectmax(top, nexttop)
                    break
            n+=1
            top=nexttop
        if maxn<s:
            maxn=s

    return maxn

N = int(input())
tarr=[list(map(int, input().split())) for _ in range(N)]
arr=[[i[0],i[5],i[1],i[3],i[2],i[4]] for i in tarr]
maxn=0

print(select(N, maxn))
