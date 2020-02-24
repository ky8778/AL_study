N, M = map(int, input().split())
Cards = list(map(int, input().split()))
max_sum = 0

for i in range(len(Cards)):
    for j in range(i+1, len(Cards)):
        for k in range(j+1, len(Cards)):
            if Cards[i]+Cards[j]+Cards[k] <= M and max_sum < Cards[i]+Cards[j]+Cards[k]:
                max_sum = Cards[i]+Cards[j]+Cards[k]
print(max_sum)

################################### 시간초과
# N, M = map(int, input().split())
# Cards = list(map(int, input().split()))
# result = []
# max_sum = 0
#
# for i in range(1 << len(Cards)):
#     case = []
#     for j in range(len(Cards)):
#         if i & (i << j):
#             case.append(Cards[j])
#     if len(case) == 3:
#         result.append(case)
# for r in range(len(result)):
#     num_sum = 0
#     for n in result[r]:
#         num_sum += n
#     if max_sum < num_sum:
#         max_sum = num_sum
# print(max_sum)