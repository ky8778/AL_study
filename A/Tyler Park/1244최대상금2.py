import sys
sys.stdin = open('1244.txt', 'r')

# Selection Sort처럼


T = int(input())

for tc in range(1, T+1) :
    Arr_inp, N = map(str, input().split())

    K = len(Arr)
    Stack = []
    maxx = int(''.join(Arr))

    A = Arr[:]

    print(maxx)

    print(f'#{tc} {maxx}')