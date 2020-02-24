N = int(input())
min_n = 987654321
for i in range(N):
    n_sum = 0
    n_sum += i
    nn = str(i)
    for j in nn:
        n_sum += int(j)
    if n_sum == N and min_n > n_sum:
        min_n = i
if min_n == 987654321:
    min_n = 0
print(min_n)