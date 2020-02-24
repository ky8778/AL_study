N = int(input())  #분해합
# len_N = len(str(N))
# str_N = str(N)
#216 = 198 + 1 + 9 + 8
#
arr = []
for i in range(N):
    sum = 0
    len_i = len(str(i))
    str_i = str(i)
    for j in range(len_i):
        sum += int(str_i[j])
    sum += i
    if sum == N:
        arr.append(i)
        result = min(arr)
    if len(arr) == 0 :
        result = 0
print(result)


#생성자가 없는 경우 pinrt(0)

