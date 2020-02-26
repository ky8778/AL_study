def NM(N, m):
    if len(result) == m:
        print(*result)
        return
    else:
        for i in range(1, N + 1):
            if not visited[i]:
                result.append(i)
                visited[i] = 1
                NM(N, m)
                result.remove(i)
                visited[i] = 0


N, M = map(int,input().split())
visited = [0 for _ in range(N + 1)]
visited[0] = -1
result = []
NM(N,M)