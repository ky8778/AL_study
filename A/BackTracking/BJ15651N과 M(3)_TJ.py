def NM(N,M):
    if len(result) == M:
        print(*result)
        return
    else:
        for i in range(N):
            result.append(natural_number[i])
            NM(N,M)
            result.pop()


N, M = map(int,input().split())
natural_number = [n for n in range(1, N + 1)]
result = []
NM(N,M)