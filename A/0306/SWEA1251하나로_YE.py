#하나로
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    xlist = list(map(int, input().split()))
    ylist = list(map(int, input().split()))
    E = float(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    visited = [0 for _ in range(N)]

    for now in range(N):
        nowy = ylist[now]
        nowx = xlist[now]
        for next in range(N):
            nexty = ylist[next]
            nextx = xlist[next]
            arr[now][next] = ((nowy-nexty)**2 +(nowx-nextx)**2)**(1/2)

    minsum = 987654321

    for num in range(N):
        idx = num
        summ = 0
        count = 1
        while count < N:
            visited[idx] = 1
            minn = 98765432123456789
            for next in range(N):
                if not visited[next] and arr[idx][next] and arr[idx][next]<minn:
                    minn = arr[idx][next]
                    idxx = next
            summ += minn**2*E
            idx = idxx
            count+=1
        
        if summ<minsum:
            minsum = summ
    print(f'#{tc+1} {int(minsum)}')