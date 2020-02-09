import sys
sys.stdin = open('백준_2477_참외밭.txt','r')

productivity = int(input())

drlist = []
dslist = []

aimindex = []

for i in range(6):
    dr, ds = map(int,input().split())
    drlist.append(dr)
    dslist.append(ds)

# print(drlist)
# print(dslist)
for i in range(6):
    if drlist.count(drlist[i]) == 1:
        aimindex.append(i)

# print(aimindex)
tlg = max(aimindex)

if min(aimindex) +1 == tlg:
    rst = productivity * (dslist[tlg]*dslist[tlg-1] - dslist[tlg-3]*dslist[tlg-4])

print(rst)