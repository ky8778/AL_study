import copy


def findnext(start):
    if start == 1:
        end_idx = 3
    elif start == 2:
        end_idx = 4
    elif start == 3:
        end_idx = 1
    elif start == 4:
        end_idx = 2
    elif start == 0:
        end_idx = 5
    elif start == 5:
        end_idx = 0
    return end_idx


def isdice(start_num,cnt):
    global dice
    dice_copy = copy.deepcopy(dice)
    hap = 0
    while cnt < num:
        Start_idx = dice[cnt].index(start_num)
        end_idx = findnext(Start_idx)
        end_num = dice[cnt][end_idx]
        dice_copy[cnt].remove(start_num)
        dice_copy[cnt].remove(end_num)
        hap += max(dice_copy[cnt])
        start_num = end_num
        cnt += 1
    return hap


num = int(input())
dice = [list(map(int,input().split())) for _ in range(num)]
result = []
for start_idx in range(6):
    start_num = dice[0][start_idx]
    result.append(isdice(start_num,0))
print(max(result))