import sys
sys.stdin = open('14888.txt', 'r', encoding='UTF-8')

def Permutation(now,end):
    # if now == end:
    #     temp = [0] * end
    #     for i in range(end):
    #         temp[i] = operators[case[i]]
    #     if temp not in case_list:
    #         case_list.append(temp)
    # else:
    #     check_list = [0] * end
    #     pick_list = [0] * end
    #
    #     for check in range(now):
    #         check_list[case[check]] = 1
    #
    #     poss = 0
    #     for check2 in range(len(check_list)):
    #         if check_list[check2] == 0:
    #             pick_list[poss] = check2
    #             poss += 1
    #
    #     for index in range(poss):
    #         case[now] = pick_list[index]
    #         Permutation(now+1,end)
    if now == end:
        case = operators[:]
        case_list.append(case)
    else:
        for change in range(now,end):
            operators[change],operators[now] = operators[now],operators[change]
            Permutation(now+1,end)
            operators[change],operators[now] = operators[now],operators[change]

def Calculator(n1,n2,op):
    if op == 0:
        return n1 + n2
    elif op == 1:
        return n1 - n2
    elif op == 2:
        return n1 * n2
    elif op == 3:
        if n1 >= 0:
            return  n1 // n2
        else:
            return -(abs(n1) // n2)

num_num = int(input())
num_list = list(map(int,input().split()))
oper_info = list(map(int,input().split()))
operators = []

for o in range(4):
    for k in range(oper_info[o]):
        operators.append(o)

case_list = []
# case = [4] * len(operators)
Permutation(0,len(operators))
print(len(case_list))
print(case_list)
max_result = -9876543210
min_result = 9876543210
for candi in range(len(case_list)):
    temp = num_list[0]
    for i in range(num_num-1):
        temp = Calculator(temp,num_list[i+1],case_list[candi][i])
    if temp < min_result:
        min_result = temp
    if temp > max_result:
        max_result = temp
print(max_result)
print(min_result)