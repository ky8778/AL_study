N = 216

ans = 0
for i in range(N) :
    temp = i
    a = str(i)

    for j in range(len(a)) :
        temp += int(a[j])

    if temp == N :
        ans = i
        break

print(ans)