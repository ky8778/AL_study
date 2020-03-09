# def getsum(score):

#     length = len(score)
#     for i in range(1 << length):
#         hap = []
#         for j in range(length + 1):
#             if i & (1 << j):
#                 hap.append(score[i])
#         result.append(sum(hap))


# T = int(input())
# for tc in range(1,T + 1):
#     N = int(input())
#     result = []
#     score = list(map(int,input().split()))
#     getsum(score)
#     result = set(result)
#     print('#{} {}'.format(tc,len(result)))


# def Bit_Array(Arr):

#     length = len(Arr)
#     for i in range(1<<length):
#         num = []
#         for j in range(length + 1):
#             if i & (1 << j):
#                 num.append(Arr[j])
#         result.append(sum(num))

# T = int(input())
# for tc in range(1,T + 1):
#     N = int(input())
#     result = []
#     score = list(map(int,input().split()))
#     Bit_Array(score)
#     result = set(result)
#     print('#{} {}'.format(tc,len(result)))




def getsum(k,N,hap):
    global result
    if sum(hap) in result:
        return
    
    if k == N:
        result.append(sum(hap))
        return

    else:
        hap.append(score[k])
        getsum(k + 1, N, hap)
        hap.pop()
        getsum(k + 1, N, hap)

T = int(input())
for tc in range(1,T + 1):
    N = int(input())
    score = list(map(int,input().split()))
    result = []
    getsum(0,N,[])
    print('#{} {}'.format(tc,len(result)))

# T = int(input())
# for tc in range(1,T + 1):
#     N = int(input())
#     score = list(map(int,input().split()))
#     result = {0}
#     for i in score:
#         plus = set()
#         for j in result:
#             plus.add(i + j)
#         result = result | plus
#     print('#{} {}'.format(tc,len(result)))

