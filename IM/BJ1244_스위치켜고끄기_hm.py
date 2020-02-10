#런타임 코드 뜯어보기

import sys
sys.stdin = open('백준_1244_스위치켜고끄기.txt','r')

def limit(cdn,len):
    if len //2 > cdn:
        return cdn
    elif len // 2 <= cdn:
        return len - cdn +1


schN = int(input()) # 1 <= schN <= 100 (=len(first))
first = list(map(int, input().split())) # [0 1 0 1 0 0 0 1]
stdN = int(input()) # 1 <= stdN <= 100
 
for i in range(stdN): #학생수이니 두번 반복
    stse, cdN = map(int, input().split())

    if stse == 1: #male
        for j in range(1,schN+1): #1~8
            if cdN * j <= len(first):
                first[cdN*j-1] = 1 - first[cdN*j-1]
            else:
                break 

    elif stse == 2: #female
        first[cdN-1] = 1 - first[cdN-1]
        for j in range(1,limit(cdN,len(first))):
            if first[cdN-1+j] == first[cdN-1-j]:
                first[cdN-1+j] = 1 - first[cdN-1+j]
                first[cdN-1-j] = 1 - first[cdN-1-j]
            else:
                break

print(*first[0:20])
print(*first[20:40])
print(*first[40:60])
print(*first[60:80])
print(*first[80:100])

# a = schN // 20
# b = schN % 20
# for i in range(a):
#     print(first[(20 * i):(20 * (i + 1))])
# print(first[(20*i):b])