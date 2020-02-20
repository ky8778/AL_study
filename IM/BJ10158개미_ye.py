#개미
w, h =map(int, input().split())
p, q =map(int, input().split())
t=int(input())

X= t%(w*2)
Y=t%(h*2)
dx=dy=1

for i in range(X):
    if p==0 or p==w:
        dx*=-1
    p+=dx

for i in range(Y):
    if q==0 or q==h:
        dy*=-1
    q+=dy

print(p,q)




