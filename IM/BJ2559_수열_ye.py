N, K = map(int, input().split())
tlist=list(map(int, input().split()))
maxn=-12345
<<<<<<< HEAD
for n in range(N-K):
    summ=0
    for k in range(K):
        if tlist[n+k]<0:
            break
        summ+=tlist[n+k]
    if summ>maxn:
        maxn=summ
=======
summ=0
for i in range(0,K):
    summ+=tlist[i]
if summ>maxn:
    maxn=summ
n=0
while n<=N-K-1:
    summ=summ-tlist[n]+tlist[n+K]
    if summ>maxn:
        maxn=summ
    n+=1

>>>>>>> dfb2e8f8d1eb80de2d0643043148fc24335ddf8c
print(maxn)