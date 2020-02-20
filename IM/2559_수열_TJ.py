total_day, day = map(int, input().split())
day_temp = list(map(int, input().split()))

temp_sum = day_temp[0:day]
max_num = sum(temp_sum)
mid_sum = max_num
for i in range(1, total_day - day + 1):
    mid_sum += - day_temp[i - 1] + day_temp[i + day - 1]
    if max_num < mid_sum:
        max_num = mid_sum

print(max_num)
