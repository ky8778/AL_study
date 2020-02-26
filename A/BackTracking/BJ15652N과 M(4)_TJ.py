def NM(N, m):
    if len(result) == m:
        print(*result)
        return
    else:
        for i in range(1, N + 1):
            if len(result) == 0 or result[-1] <= i:
                result.append(i)
                NM(N,m)
                result.remove(i)


N, M = map(int,input().split())
result = []
NM(N,M)
