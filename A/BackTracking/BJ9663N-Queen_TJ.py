def N_Queen(n):
    global cnt
    if n == N:
        cnt += 1
        return
    else:
        for i in range(N):
            if not visited[i] and not visited_plus[n + i] and not visited_minus[n - i + N]:
                visited[i] = visited_plus[n + i] = visited_minus[n - i + N] = True
                N_Queen(n + 1)
                visited[i] = visited_plus[n + i] = visited_minus[n - i + N] = False


N = int(input())
visited = [0 for _ in range(N)]
visited_plus = [0 for _ in range(2*N)]
visited_minus = [0 for _ in range(2*N)]
cnt = 0
N_Queen(0)
print(cnt)