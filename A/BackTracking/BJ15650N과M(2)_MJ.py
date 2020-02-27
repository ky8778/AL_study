# user_input = input()
#
# N, M = map(int, user_input.split(' '))
# numbers = list(range(1, N + 1))
# num_all = 1
# for i in range(N, M, -1):
#     num_all *= i
# for j in range(M, 0, -1):
#     num_all //= j
#
#
# def track(depth, ans):
#     if depth == M:
#         result = list(map(str, ans))
#         compare_lst = result.sort()
#         for k in range(num_all):
#             if result[k] == compare_lst[k]:
#             print(' '.join(result))
#             return
#     for number in numbers:
#         if number in ans:
#             continue
#         else:
#             ans.append(number)
#             track(depth + 1, ans)
#             ans.pop()
# track(0,[])

user_input = input()

N, M = map(int, user_input.split(' '))
numbers = list(range(1, N + 1))


def track(depth, ans):
    if depth == M:
        result = list(map(str, ans))
        for i in range(M-1):
            if result[i] > result[i+1]:
                break
        else:
            print(' '.join(result))
        return
    for number in numbers:
        if number in ans:
            continue
        else:
            ans.append(number)
            track(depth + 1, ans)
            ans.pop()
track(0,[])