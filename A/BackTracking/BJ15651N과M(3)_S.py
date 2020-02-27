def Sequence(depth):
    if depth == M:
        print(*result)
        return
    for n in range(N):
        result.append(num[n])
        Sequence(depth + 1)
        result.pop()


N, M = map(int, input().split())
num = list(range(1, N + 1))
result = []

Sequence(0)