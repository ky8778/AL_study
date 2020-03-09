import sys
sys.stdin = open('보물상자 비밀번호.txt','r')


number = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}


def getresult(n):
    global num_list
    for i in range(4):
        hap, cnt = 0, 0
        for j in range(n*(i + 1) -1, n*i - 1, -1):
            hap += number[num16[j]] * (16**cnt)
            cnt += 1
        num_list.add(hap)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int,input().split())
    num16 = list(input())
    num_list = set()
    for i in range(N//4):
        getresult(N//4)
        num = num16.pop()
        num16.insert(0,num)

    num_list = list(num_list)
    num_list.sort(reverse = True)
    print('#{} {}'.format(tc,num_list[K-1]))



# def getresult(n):
#     global num_list
#     for i in range(4):
#         hap = ''
#         for j in range(n*i, n*(i + 1)):
#             hap += num16[j]
#         num_list.add(hap)


# def transform(n):
#     for i in num_list:
#         cnt = len(i) - 1
#         hap = 0
#         for j in range(cnt):
#             hap += number[i[j]]*(16**(n - j - 1))
#         result.append(hap)
            



# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int,input().split())
#     num16 = list(input())
#     num_list = set()

#     for i in range(N//4):
#         getresult(N//4)
#         num = num16.pop()
#         num16.insert(0,num)

#     num_list = list(num_list)
#     result = []
#     transform(N//4)
#     print(result)