def FindBingo(Check):
    global Bingo
    # 가로 빙고 찾기
    cnt2 = 0
    for i in range(5):
        cnt1 = 0
        for j in range(5):
            if int(Check[i][j]):
                cnt1 += 1
        if cnt1 == 5:
            Bingo += 1
        if int(Check[i][i]):
            cnt2 += 1
    if cnt2 == 5:
        Bingo += 1
    return

Chulsu = [list(map(int, input().split())) for _ in range(5)]
MC = []
for _ in range(5):
    MC += list(map(int, input().split()))
Check = [[0] * 5 for _ in range(5)]
Bingo = k = result = 0

while Bingo < 3 and k < 25:
    Bingo = 0
    v_Check = []
    for n in range(5):
        for m in range(5):
            if MC[k] == Chulsu[n][m]:
                Check[n][m] = 1
                break
    for m in range(4, -1, -1):
        v = ''
        for n in range(5):
            v += str(Check[n][m])
        v_Check.append(v)

    FindBingo(Check)
    FindBingo(v_Check)
    if Bingo >= 3:
        result = k+1
        break
    k += 1

print(result)


# def Bingo(Check):
#     # 가로 빙고 찾기
#     for i in range(5):
#         cnt = 0
#         for j in range(5):
#             if Check[i][j]:
#                 cnt += 1
#             else:
#                 break
#         if cnt == 5:
#             return True
#     # 세로 빙고 찾기
#     for j in range(5):
#         cnt = 0
#         for i in range(5):
#             if Check[i][j]:
#                 cnt += 1
#             else:
#                 break
#         if cnt == 5:
#             return True
#     # 증가 대각선 빙고 찾기
#     cnt = j = 0
#     i = 4
#     while j < 5:
#         if Check[i][j]:
#             cnt += 1
#         i -= 1
#         j += 1
#     if cnt == 5:
#         return True
#     # 감소 대각선 빙고 찾기
#     cnt = 0
#     i = j = 4
#     while j >= 0:
#         if Check[i][j]:
#             cnt += 1
#         i -= 1
#         j -= 1
#     if cnt == 5:
#         return True
#
#
# Chulsu = [list(map(int, input().split())) for _ in range(5)]
# Check = [[0]*5 for __ in range(5)]
# MC = []
# for _ in range(5):
#     MC += list(map(int, input().split()))
# Bingo_cnt = 0
# result = 0
#
# for k in range(len(MC)):
#     for n in range(5):
#         for m in range(5):
#             if MC[k] == Chulsu[n][m]:
#                 Check[n][m] = True
#             if Bingo(Check):
#                 Bingo_cnt += 1
#             if Bingo_cnt == 3:
#                 result = k+1
#                 break
#         if result > 0:
#             break
#     if result > 0:
#         break
# print(result)

'''
for _ in range(5):
    line = list(map(int, input().split()))
    for __ in range(5):
        counting.append(line[__])

for count in counting:
    for i in range(5):
        for j in range(5):
            if chulsu[i][j] == count:
                cnt += 1
                answer[i][j] = cnt

while bingo < 3:
    for i in range(5):
        for j in range(5):
            check_v += 
            check_h

def FindBingo(chulsu, counting):
    Bingo = cnt = 0
    check_v = [0] * 5
    check_h = [0] * 5
    for count in counting:
        for i in range(5):
            for j in range(5):
                if chulsu[i][j] == count:
                    check_v[i] += 1
                    check_h[i] += 1
                if check_v[i] == 5:
                    if Bingo == 3:
                        return cnt
                    else:
                        Bingo += 1
                if check_h == 5:
                    if Bingo == 3:
                        return cnt
                    else:
                        Bingo += 1

FindBingo(chulsu, counting)
'''