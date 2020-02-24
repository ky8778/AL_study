import sys
sys.stdin = open('2798.txt', 'r')

N, M = map(int, input().split()) #카드 개수 N, 최대 합 M
num_lst = list(map(int, input().split()))

new_arr = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if num_lst[i] + num_lst[j] + num_lst[k] <= M:
                new_arr.append(num_lst[i] + num_lst[j] + num_lst[k])

print(max(new_arr))

