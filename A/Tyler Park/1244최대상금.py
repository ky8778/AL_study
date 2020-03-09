import sys
sys.stdin = open('1244.txt', 'r')

# K = len(Arr)
# 2개씩 N번 선택
# N번 교환하고 값 확인




def INP(inp) :
    if len(inp) == 1 :
        return int(inp)
    else :
        return list(map(str, inp))


def SELECT(d = 0) :

    if Stack :
        CHANGE()
        return

    for i in range(K) :
        for j in range(i+1, K) :
            Stack.append(i)
            Stack.append(j)
            SELECT(d+1)
            Stack.pop()
            Stack.pop()

def CHANGE() :
    global maxx

    A = Arr[:]
    for i in range(0, N, 2) :
        A[Stack[i]], A[Stack[i+1]] = A[Stack[i+1]], A[Stack[i]]

    A2 = int(''.join(A))
    if A2 > maxx : maxx = A2


T = int(input())

for tc in range(1, T+1) :
    Arr, N = map(INP, input().split())
    K = len(Arr)
    Stack = []
    maxx = int(''.join(Arr))

    A = Arr[:]
    SELECT()

    print(f'#{tc} {maxx}')