#vs에서 되는데 틀렸습니다.

import sys
sys.stdin = open('백준_2578_빙고.txt','r')

my_board = []
for i in range(5):
    my_board += [list(map(int,input().split()))]

# print(my_board)

call = []
for i in range(5):
    call += list(map(int,input().split()))

print(call)

ch = [[0 for _ in range(5)] for __ in range(5)]

print(ch)



for i in range(25):                             # call[i] = 사회자가 i+1번째 부르는 번호들
    for j in range(5):
        for k in range(5):
            if call[i] == my_board[j][k]:
                ch[j][k] = 1                    # 여기서 사회자가 부른 값에 대한 체크가 됨

    cnt = 0                                     # cnt는 빙고 줄에 개수
    a= 0
    b=0

    for j in range(5):
        if sum(ch[j]) == 5:
            cnt += 1             #중복해서 더해지는걸 어떻게 방지하지?
    for j in range(5):
        if ch[0][j] + ch[1][j] + ch[2][j] + ch[3][j] + ch[4][j] == 5:
            cnt += 1
    for j in range(5):
        a += ch[j][j]
        b += ch[j][4-j]
    if b == 5:
        cnt+=1
    if a == 5:
        cnt+=1
    
    if cnt == 3:
        print(i+1)
        break