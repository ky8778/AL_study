space = [[0]*101 for _ in range(101)]
N = int(input())

for N in range(1, N+1):
    paper = list(map(int, input().split()))
    for i in range(paper[1], paper[1]+paper[3]):
        for j in range(paper[0], paper[0] + paper[2]):
            space[i][j] = N
for N in range(1, N+1):
    cnt = 0
    for r in range(101):
        for c in range(101):
            if space[r][c] == N:
                cnt += 1
    print(cnt)