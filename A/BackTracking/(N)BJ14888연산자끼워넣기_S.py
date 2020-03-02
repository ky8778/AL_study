# 1. input된 연산자의 개수를 사용해 연산자를 나열한다.( ex)C = ['+','*']...)
# 2. 나열된 연산자를 가지고 순서를 바꾸는 경우의 수를 확인한다.(Ifcal())
# 3. 각 경우의 수 마다 계산을 하고, 최대값인지 혹은 최솟값인지 확인한다.(Calculate())
# 4. 답을 출력한다.

# 왜 틀려? 아ㅏㅏㅏㅏㅏㅏㅏ;ㅣㅏㅣ;;;

def Ifcal(depth):
    global Cal, Check
    if depth == (N-1):
        Calculate(Cal)
        return
    for i in range(N-1):
        if i not in Check:
            Check += [i]
            Cal += [C[i]]
            Ifcal(depth+1)
            Cal.pop()
            Check.pop()

def Calculate(lst):
    global max_cal, min_cal
    Num = []
    Num += Number
    for i in range(N-1):
        if Cal[i] == '+':
            Num[i+1] = Num[i] + Num[i+1]
        elif Cal[i] == '-':
            Num[i+1] = Num[i] - Num[i+1]
        elif Cal[i] == '*':
            Num[i+1] = Num[i] * Num[i+1]
        elif Cal[i] == '/':
            if Num[i] > 0:
                Num[i+1] = Num[i] // Num[i+1]
            else:
                Num[i+1] = (abs(Num[i]) // Num[i+1]) * (-1)

    if min_cal > Num[-1]:
        min_cal = Num[-1]
    if max_cal < Num[-1]:
        max_cal = Num[-1]


N = int(input())
Number = list(map(int, input().split()))
Cal_info = list(map(int, input().split()))
Calculator = ['+', '-', '*', '/']
C = []
Cal = []
Check = []
min_cal = 987654321
max_cal = 0

for i in range(4):
    I = Cal_info[i]
    while I > 0:
        I -= 1
        C += [Calculator[i]]

Ifcal(0)

print(max_cal)
print(min_cal)

# def Index(depth):
#     global C_index, L
#     LL = []
#     if depth == len(C):
#         LL += L
#         C_index.append(LL)
#         return
#     for i in range(len(C)):
#         if i not in L:
#             L += [i]
#             Index(depth+1)
#             L.pop()
#
# def Calculate(n):
#     if C[C_index[j][n]] == '+':
#         Num[n+1] = Num[n] + Num[n+1]
#     if C[C_index[j][n]] == '-':
#         Num[n + 1] = Num[n] - Num[n + 1]
#     if C[C_index[j][n]] == '*':
#         Num[n + 1] = Num[n] * Num[n + 1]
#     if C[C_index[j][n]] == '/':
#         if Num[n] > 0:
#             Num[n+1] = Num[n] // Num[n+1]
#         else:
#             Num[n+1] = (((-1) * Num[n]) // Num[n+1]) * (-1)
#
#
# N = int(input())
# Number = list(map(int, input().split()))
# Cal_num = list(map(int, input().split()))
# lst = ['+', '-', '*', '/']
# C = []
# C_index = []
# L = []
# min_cal = 987654321
# max_cal = 0
#
# for a in range(4):
#     A = Cal_num[a]
#     while A > 0:
#         A -= 1
#         C += [lst[a]]
#
# Index(0)
#
# for j in range(len(C_index)):
#     Num = []
#     Num += Number
#     for i in range(len(C)):
#         Calculate(i)
#     if min_cal > Num[-1]:
#         min_cal = Num[-1]
#     if max_cal < Num[-1]:
#         max_cal = Num[-1]
#
# print(max_cal)
# print(min_cal)
