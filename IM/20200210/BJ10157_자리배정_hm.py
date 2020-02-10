# 런타임에러

# def isSafy (y,x):
#     if y >=0 and y<=R and x >=0 and y <=C:
#         return True

import sys
sys.stdin = open('백준_10157_자리배정.txt','r')

C, R = map(int, input().split()) # 7,6
tl = int(input())

zero = [[0 for _ in range(C)] for __ in range(R)]

cnt = 0

x=0 #6
y=R-1 #5

while cnt != tl:
    while zero[y-1][x] != 1:
        zero[y][x] = 1
        cnt += 1
        if cnt == tl:
            print('{} {}'.format(x+1,6-y))
            break
        y -= 1


    for i in range(C-1):
        zero[y][x] = 1
        cnt +=1
        if cnt == tl:
            print('{} {}'.format(x+1,6-y))
            break
        x += 1
    x += 1
    for i in range(R-1):
        zero[y][x] = 1
        cnt +=1
        if cnt == tl:
            print('{} {}'.format(x+1,6-y))
            break
        y += 1

    while zero[y][x-1] != 1:
        zero[y][x] = 1
        cnt += 1
        if cnt == tl:
            print('{} {}'.format(x+1,6-y))
            break
        x -= 1
    break