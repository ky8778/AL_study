w,h=map(int, input().split())
lnum = int(input())
hlist=[0,h]
wlist=[0,w]

for i in range(lnum):
    n, t = map(int, input().split())
    if n==0:
        hlist.append(t)
    else:
        wlist.append(t)

hlist.sort()
wlist.sort()

htemp=[hlist[k+1]-hlist[k] for k in range(len(hlist)-1)]
wtemp=[wlist[k+1]-wlist[k] for k in range(len(wlist)-1)]

print(max(htemp)*max(wtemp))


    