import sys
sys.stdin = open('7568.txt', 'r')

N = int(input())

Weight = [0] * N
Height = [0] * N

for i in range(N) :
    Weight[i], Height[i] = map(int, input().split())

# 자신보다 큰 사람의 수를 저장
Rank = [1] * N

for i in range(N) :
    W1, H1 = Weight[i], Height[i]

    for j in range(i+1, N) :
        W2, H2 = Weight[j], Height[j]

        if W1 > W2 and H1 > H2 :
            Rank[j] += 1

        elif W1 < W2 and H1 < H2 :
            Rank[i] += 1

print(*Rank)