#방배정

N, K = map(int, input().split())
blist = [0 for _ in range(7)]
glist = [0 for _ in range(7)]
count=0
for n in range(N):
    s, a=map(int, input().split())
    if s==1:#남
        blist[a]+=1
    else:#여
        glist[a]+=1

for t in range(1, len(blist)):
    if blist[t] ==0 and glist[t]==0:
        continue
    elif blist[t]==0:
        count += (glist[t] // K)
        if glist[t]%K>0:
            count+=1

    elif glist[t]==0:
        count += (blist[t] // K)
        if blist[t] % K > 0:
            count += 1
    else:
        count += (blist[t] // K) + (glist[t] // K)
        if blist[t]%K>0:
            count+=1
        if glist[t]%K >0:
            count+=1

print(count)


