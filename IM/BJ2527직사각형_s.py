T = 4
while T > 0:
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if p1 < x2 or q1 < y2 or x1 > p2 or y1 > q2:
        print('d')    # 떨어져 있음
    elif (x1 == p2 or p1 == x2)and (q1 == y2 or y1 == q2):
        print('c')    # 점
    elif x1 == p2 or y1 == q2 or p1 == x2 or q1 == y2:
        print('b')    # 선분
    else:
        print('a')    # 겹침
    T -= 1






