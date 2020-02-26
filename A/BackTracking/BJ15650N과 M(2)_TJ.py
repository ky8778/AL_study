def NM(N, m):
    if len(result) == m:
        print(*result)
        return
    else:
        for i in range(1, N + 1):
            if not visited[i]:
                if len(result) == 0 or result[-1] <= i:
                    result.append(i)
                    visited[i] = 1
                    NM(N,m)
                    result.remove(i)
                    visited[i] = 0


N, M = map(int,input().split())
visited = [0] * (N+1)
result = []
NM(N,M)