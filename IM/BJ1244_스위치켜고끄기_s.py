# 런타임에러가 나오면 '백준 런타임에러' 검색해보기
# control+d 하면 변수이름 한번에 변경 가능
switchs, switch = int(input()), list(map(int, input().split()))
students = int(input())
count = [0]*len(switch)
for i in range(students):
    g, n = list(map(int, input().split()))
    if g == 1:
        for j in range(1, (len(switch)//n)+1):
            count[j*n] += 1
    else:
        if n > len(switch)/2:
            where = len(switch) - n
        else:
            where = n - 1
        for j in range(1, where + 1):
            if switch[n-j] == switch[n+j]:
                count[n-j] += 1
                count[n+j] += 1
del count[0]
for i in range(len(switch)):
    if switch[i] == 1 and count[i] % 2:
        switch[i] = 0
    elif switch[i] == 0 and count[i] % 2:
        switch[i] = 1
print(switch)



