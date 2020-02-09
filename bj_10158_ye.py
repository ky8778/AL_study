#개미
w, h =map(int, input().split())
p, q =map(int, input().split())
t=int(input())
def banbok(tempp, tempq, dx,dy):
    if tempp==p and tempq==q and dx==1 and dy==1 and i!=1:
        return True

def ant(t):
    dx=dy=1
    global tempp, tempq
    for i in range(1,t+1):
        if banbok(tempp, tempq,dx,dy):
            return t%i
        if tempp==0 or tempp==w:
            dx*=-1
        elif tempq==0 or tempq==h:
            dy*=-1
        tempp+=dx
        tempq+=dy
    return [tempp,tempq]
tempp=p
tempq=q
i=1
anwlist=[]
while True:
    if type(ant(t))=="<class 'int'>":
        anwlist=ant(ant(tempp, tempq))
    else: anwlist+=ant(t)

print(*anwlist)