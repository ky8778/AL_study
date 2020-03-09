import sys
sys.stdin = open('5099.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    C_idx = [i for i in range(len(C))]

    Oven = []

    for i in range(N):
        Oven.append(C_idx.pop(0))

    now = -1
    cnt = 0
    ans = 0

    while True:
        now = (now + 1) % N
        i = Oven[now]

        if C.count(0) == len(C) - 1 and i != -1:
            ans = i + 1
            break

        if i != -1 :
            C[i] = C[i] // 2

        if i != -1 and not C[i]:
            cnt += 1
            if C_idx: Oven[now] = C_idx.pop(0)
            else : Oven[now] = -1

    print(f'#{tc} {ans}')




