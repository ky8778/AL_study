import sys
sys.stdin = open('영준이의카드카운팅.txt', 'r')
#겹치는 카드 가지고 있으면 ERROR출력
#A:1 / 2~10 / J:11 / Q:12 / K:13  // 무늬별로 13장씩

T = int(input())
for tc in range(1, T+1):
    card_lst = input()
    S_num = 13
    D_num = 13
    H_num = 13
    C_num = 13
    count = 0
    flag = 1
    for j in range(0, len(card_lst), 3):
        if card_lst[j:j+3] in card_lst[j+3:]:
            print('#%d ERROR' %(tc))
            flag = 0
            break


    for i in range(len(card_lst)):

        if card_lst[i] == 'S':
            S_num -= 1
        if card_lst[i] == 'D':
            D_num -= 1
        if card_lst[i] == 'H':
            H_num -= 1
        if card_lst[i] == 'C':
            C_num -= 1
    if flag:
        print('#%d' %(tc), end = ' ')
        print('%d %d %d %d' % (S_num, D_num, H_num, C_num))


 # 0, 3, 6, 9
