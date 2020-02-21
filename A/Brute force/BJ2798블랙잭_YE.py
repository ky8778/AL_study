#블랙잭 _ 브루트포스 버전
N,M = map(int, input().split())
Card = list(map(int, input().split()))
maxn=0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            tnum=Card[i]+Card[j]+Card[k]
            if tnum>maxn and tnum<=M:
                maxn=tnum

print(maxn)