def nQueen(i):
    global cnt
    if i == N:
        cnt += 1
        return
    for j in range(N):
        if not visited[j] and not visited_I[i+j] and not visited_D[i-j+N]:
            visited[j] = visited_I[i+j] = visited_D[i-j+N] = 1
            nQueen(i+1)
            visited[j] = visited_I[i+j] = visited_D[i-j+N] = 0


N = int(input())
visited = [0]*N
visited_I = [0]*(N*2)
visited_D = [0]*(N*2)
cnt = 0

nQueen(0)
print(cnt)

# def nQueen(i):
#     global cnt
#     if i == N:
#         cnt += 1
#         return
#     for j in range(N):
#         if not visited[j] and not visited_I[i+j] and not visited_D[i-j+N]:
#             visited[j] = visited_I[i+j] = visited_D[i-j+N] = 1
#             nQueen(i+1)
#             visited[j] = visited_I[i+j] = visited_D[i-j+N] = 0
#
#
# N = int(input())
# visited = [0]*N
# visited_I = [0]*(N*2)
# visited_D = [0]*(N*2)
# cnt = 0
#
# nQueen(0)
# print(cnt)
