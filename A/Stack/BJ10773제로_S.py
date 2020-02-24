# K = int(input())
# stack = [0]*K
# top = -1
# num_sum = 0
#
# while K > 0:
#     K -= 1
#     num = int(input())
#     if num:
#         top += 1
#         stack[top] = num
#         num_sum += num
#     else:
#         num_sum -= stack[top]
#         del stack[top]
#         top -= 1
#
# print(num_sum)

K = int(input())
stack = []
num_sum = 0

while K > 0:
    K -= 1
    num = int(input())
    if num:
        stack.append(num)
        num_sum += num
    else:
        num_sum -= stack[-1]
        stack.pop()

print(num_sum)
