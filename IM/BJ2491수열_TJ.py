length = int(input())
num_list = list(map(int, input().split()))

max_num1 = 0
cnt1 = 1

for i in range(1, length):
    if num_list[i-1] <= num_list[i]:
        cnt1 += 1
        if i == length - 1 and cnt1 > max_num1:
            max_num1 = cnt1
    else:
        if max_num1 < cnt1:
            max_num1 = cnt1
            cnt1 = 1
        else:
            cnt1 = 1

max_num2 = 0
cnt2 = 1
for i in range(1, length):
    if num_list[i-1] >= num_list[i]:
        cnt2 += 1
        if i == length - 1 and cnt2 > max_num2:
            max_num2 = cnt2
    else:
        if max_num2 < cnt2:
            max_num2 = cnt2
            cnt2 = 1
        else:
            cnt2 = 1

if length == 1:
    max_num1 = max_num2 = 1

print(max(max_num1, max_num2))