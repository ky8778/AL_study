T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Arr = list(map(int, input().split()))

    print(f'#{tc} {Arr[M % N]}')
