import sys
sys.stdin = open('7568.txt', 'r')

T = int(input()) #사람 수
lst = [list(map(int, input().split())) for _ in range(T)]  #몸무게, 키
score_lst = [1] * T
count = 0
for i in range(T): #01234
    for j in range(T): # 01234
        # if i + j > 4 :
        #     break
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            score_lst[i] += 1
print(*score_lst)





    #print(score)  #공백으로 이어서 등수 출력