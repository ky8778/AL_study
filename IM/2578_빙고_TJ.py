def bingo(a):
    for n in range(5):
        for m in range(5):
            if bingo_before[n][m] == a:
                bingo_before[n][m] = '*'
                return True
    return False


def search(b):
    cnt = 0
    cnt1 = 0
    cnt2 = 0
    for y in range(5):
        cnt3 = 0
        if b[y] == ['*', '*', '*', '*', '*']:
            cnt += 1
        if b[y][y] == '*':
            cnt1 += 1
            if cnt1 == 5:
                cnt += 1
        if b[y][4-y] == '*':
            cnt2 += 1
            if cnt2 == 5:
                cnt += 1
        for x in range(5):
            if b[x][y] == '*':
                cnt3 += 1
            if cnt3 == 5:
                cnt += 1
    if cnt >= 3:
        return True
    return False

bingo_before = []
for i in range(5):
    write_num = list(map(int, input().split()))
    bingo_before.append(write_num)

bingo_start = []
for i in range(5):
    talk_num = list(map(int, input().split()))
    bingo_start.append(talk_num)

num = 0
i = 0
j = 0
while True:
    if search(bingo_before):
        print(num)
        break
    elif bingo(bingo_start[i][j]):
        num += 1
        j += 1
        if j == 5:
            j = 0
            i += 1