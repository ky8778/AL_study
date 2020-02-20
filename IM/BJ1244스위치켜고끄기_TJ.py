Switch_num = int(input())
Switch_list = list(map(int, input().split()))
Student_num = int(input())

for i in range(Student_num):
    Student = list(map(int, input().split()))

    for j in range(Switch_num):
        if Student[0] == 1 and (j % Student[1]) +1 == Student[1]:
            Switch_list[j] = 1 - Switch_list[j]
        elif Student[0] ==2 and j + 1 == Student[1]:
            cnt = 0
            while j - cnt >= 0 and j + cnt < Switch_num:
                if cnt == 0:
                    Switch_list[j] = 1 - Switch_list[j]
                    cnt += 1
                elif Switch_list[j - cnt] == Switch_list[j + cnt]:
                    Switch_list[j - cnt] = 1 - Switch_list[j - cnt]
                    Switch_list[j + cnt] = 1 - Switch_list[j + cnt]
                    cnt += 1
                else:
                    break
result = ''
for i in range(Switch_num):
    result += str(Switch_list[i]) + ' '
    if (i + 1) % 20 == 0:
        print(result[:-1])
        result = ''
print(result[:-1])