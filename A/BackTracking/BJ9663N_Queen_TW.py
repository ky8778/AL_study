N = int(input())

def DFS(r) :
    global cnt
    if r == N : cnt += 1 ; return

    for c in range(N) :
        if not C[c] and not D1[r+c] and not D2[r-c+N-1] :
            C[c] = 1
            D1[r+c] = 1
            D2[r-c+N-1] = 1

            DFS(r+1)
            C[c] = 0
            D1[r + c] = 0
            D2[r-c+N-1] = 0

C = [0] * N
D1 = [0] * (2*N-1) # r + c - 1
D2 = [0] * (2*N-1) # c - r + N - 1

cnt = 0
DFS(0)
print(cnt)