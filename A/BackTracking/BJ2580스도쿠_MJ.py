import sys
sys.stdin = open('2580.txt', 'r', encoding='UTF-8')

def sdoku(now,end):
    global flag
    if now == end:
        for p in range(9):
            print(*map_matrix[p])
        flag = 1
        return
    else:
        y, x = empty_list[now]
        box_check = 3 * (y // 3) + x // 3
        for num in possible_list[now]:
            if (num not in map_matrix[y]) and (num not in x_check_map[x]) and (num not in box_check_map[box_check]):
                map_matrix[y][x] = num
                x_check_map[x][y] = num
                box_check_map[box_check][3 * (y % 3) + (x % 3)] = num
                sdoku(now+1,end)
                if flag:
                    return
                else:
                    map_matrix[y][x] = 0
                    x_check_map[x][y] = 0
                    box_check_map[box_check][3 * (y % 3) + x % 3] = 0

map_matrix = [list(map(int,input().split())) for _ in range(9)] # 원본
x_check_map = list([0]*9 for _ in range(9))
box_check_map = []
for start_y in range(0,9,3):
    for start_x in range(0,9,3):
        temp = []
        for k in range(3):
            temp.extend(map_matrix[start_y+k][start_x:start_x+3])
        box_check_map.append(temp)
for idy in range(9):
    for idx in range(9):
        x_check_map[idx][idy] = map_matrix[idy][idx]
empty_list = []
for idy in range(9):
    for idx in range(9):
        if not map_matrix[idy][idx]:
            empty_list.append((idy,idx))
possible_list = [ [] for _ in range(len(empty_list))]
for index in range(len(empty_list)):
    y, x = empty_list[index]
    box_check = 3 * (y // 3) + x // 3
    for num in range(1, 10):
        if (num not in map_matrix[y]) and (num not in x_check_map[x]) and (num not in box_check_map[box_check]):
            possible_list[index].append(num)
flag = 0
# for first in range(len(empty_list)-1):
#     my_index = first
#     for second in range(first+1,len(empty_list)):
#         if len(possible_list[my_index]) > len(possible_list[second]):
#             my_index = second
#     possible_list[my_index] , possible_list[first] = possible_list[first], possible_list[my_index]
#     empty_list[my_index] , empty_list[first] = empty_list[first], empty_list[my_index]

sdoku(0,len(empty_list))




# for p in range(9):
#     print(*map_matrix[p])
# print()
# print()
# print()
# print(empty_list)
# print(map_matrix)
# for p in range(9):
#     print(*x_check_map[p])
# print(box_check_map)