num = int(input())

length_list = []
for i in range(6):
    length = list(map(int, input().split()))
    length_list.append(length)

max_height = 0
max_length = 0
for i in range(6):
    if (length_list[i][0] == 3 or length_list[i][0] == 4) and length_list[i][1] > max_height:
        max_height = length_list[i][1]
        maxH_idx = i
    if (length_list[i][0] == 1 or length_list[i][0] == 2) and length_list[i][1] > max_length:
        max_length = length_list[i][1]
        maxL_idx = i

minH_idx = (maxL_idx + 3) % 6
minL_idx = (maxH_idx + 3) % 6

max_area = max_height * max_length
min_area = length_list[minH_idx][1]*length_list[minL_idx][1]

fruit_num = (max_area - min_area)*num
print(fruit_num)