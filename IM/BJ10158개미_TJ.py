w, h = map(int, input().split())
x, y = map(int, input().split())
hour = int(input())

if (x + hour)%(2*w) > w:
    Newx = 2*w - ((x + hour)%(2*w))
else:
    Newx = (x + hour)%(2*w)
if (y + hour)%(2*h) > h:
    Newy = 2*h - ((y + hour)%(2*h))
else:
    Newy = (y + hour)%(2*h)
print(Newx,Newy)