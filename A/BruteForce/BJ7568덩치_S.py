N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
Rank = [0] * N

for i in range(len(P)):
    k = 0
    for j in range(len(P)):
        if i != j and P[i][0] < P[j][0] and P[i][1] < P[j][1]:
            k += 1
    Rank[i] = k+1
print(*Rank)