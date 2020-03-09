import copy

def Stack(n, dice_num):
    global stack_sum, S_result
    copy_Dice = copy.deepcopy(Dice)
    for i in range(dice_num):
        n_index = Dice[i].index(n)
        m_index = Opposite(n_index)
        m = Dice[i][m_index]
        copy_Dice[i][n_index] = 0
        copy_Dice[i][m_index] = 0
        S_result += max(copy_Dice[i])
        n = m
    return

def Opposite(n):
    if n == 0:
        return 5
    if n == 1:
        return 3
    if n == 2:
        return 4
    if n == 3:
        return 1
    if n == 4:
        return 2
    if n == 5:
        return 0

dice_num = int(input())
Dice = [list(map(int, input().split())) for _ in range(dice_num)]
max_sum = 0

i = 1
while i < 7:
    S_result = 0
    Stack(i, dice_num)
    if max_sum < S_result:
        max_sum = S_result
    i += 1

print(max_sum)