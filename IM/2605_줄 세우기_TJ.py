nums = int(input())
num_list = list(map(int,input().split()))
sort_list = [1]

for i in range(1, nums):
    for j in range(i + 1):
        if num_list[i] == j:
            sort_list.insert(i - j, i+1)
print(*sort_list)