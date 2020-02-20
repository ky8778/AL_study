def isprove(y,x):
    if y[1] < y[2] or y[3] < y[0] or x[1] < x[2] or x[3] < x[0]:
        return 'd'
    elif (y[1] == y[2] or y[0] == y[3]) and (x[1] == x[2] or x[0] == x[3]):
        return 'c'
    elif y[1] == y[2] or y[0] == y[3] or x[1] == x[2] or x[0] == x[3]:
        return 'b'
    else:
        return 'a'

square = []

for i in range(4):
    dot = list(map(int, input().split()))
    square.append(dot)

dotY = []
dotX = []
for i in range(4):
    dotY = square[i][1::2]
    dotX = square[i][0::2]
    print(isprove(dotY,dotX))

