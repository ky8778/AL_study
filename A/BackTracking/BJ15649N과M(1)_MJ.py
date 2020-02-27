# N, M = map(int, input().split())
#
# for i in range(1, N+1):
#     arr = [0]*M
#     for j in range(1, N+1):
#         for k in range(M): ##
#             if i == j:
#                 continue
#             arr.append(i)
#
# #######
# #방법1
# def perm_r_1(result,now,end):
#     if now == end:
#         print(result)  # a는 출력할 결과리스트
#     else:
#         in_perm = [False] * end # 후보군 목록
#         pick_list = [0] * end
#
#         for i in range(now):
#             in_perm[result[i]] = True  # 조사한 후보군 표시
#
#         ncandidates = 0 # 가능한 후보군 숫자
#         for i in range(end):
#             if in_perm[i] == False:
#                 pick_list[ncandidates] = i
#                 ncandidates += 1
#
#         for i in range(ncandidates): # k 결과리스트 인덱스
#             result[now] = pick_list[i]
#             perm_r_1(result, now + 1 , end)
#
# result = [0] * r
# perm_r_1(result,0,end)
# #
# # #####################
# # N = 3 # 전체길이
# # R = 3  # 결과길이.몇 개 뽑을건지.
# # #arr = 만들어진 숫자 목록
#
# #방법2
# N, R = map( int, input().split())
# arr = [k for k in range(1, N+1)]
# result_list = []
# def perm_r_3(now):
#     if now == R:
#         temp = []
#         for i in range(R):
#             temp.append(arr[i])
#         result_list.append(temp)
#
#     else:
#         for change in range(now, N):
#             arr[now], arr[change] = arr[change], arr[now]
#             perm_r_3(now+1)
#             arr[now], arr[change] = arr[change], arr[now]
# perm_r_3(0)
# result_list.sort()
# for k in range(len(result_list)):
#     print(*result_list[k])
#
# ##########################################3
# #방법 3(승민이 코드)
#
# N, M = map(int, user_input.split(' '))
# numbers = list(range(1, N + 1))
#
#
# def track(start, depth, ans): #depth는 이때까지 몇개 뽑았는지. ans는 숫자 뽑은거 리스트.
#     if depth == M - 1:
#         result = list(map(str, ans))
#         print(' '.join(result))
#         return
#     for number in numbers:
#         if ans is not None:
#             if number in ans:
#                 continue
#             else:
#                 ans.append(number)
#                 track(number, depth + 1, ans)
#                 ans.pop() #재귀처리하고 원상복귀 하는거.
# for number in numbers:
#     track(number, 0, [number])


##승민이가 수정한 코드.
user_input = input()

N, M = map(int, user_input.split(' '))
numbers = list(range(1, N + 1))


def track(depth, ans):
    if depth == M:
        result = list(map(str, ans))
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