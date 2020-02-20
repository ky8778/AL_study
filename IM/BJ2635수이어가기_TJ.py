num = int(input())
max_cnt = 0
for i in range(1, num + 1):
    select = i
    num_search = num
    num_list = [num_search, select]
    cnt = 1
    while select >= 0:
        num_search, select = select, num_search - select
        num_list.append(select)
        cnt += 1

    if max_cnt < cnt:
        max_cnt = cnt
        max_list = num_list

max_list.pop()
print(max_cnt)
print(*max_list)