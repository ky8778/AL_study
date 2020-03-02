import sys
sys.stdin = open('9663.txt', 'r')

def DFS(idy):
    global count
    if idy == N:
        count += 1
    else:
        for idx in range(N):
            if not x_visited[idx] and not right_down_visited[idx-idy] and not right_up_visited[idx+idy]:
                x_visited[idx] = 1
                right_down_visited[idx-idy] = 1
                right_up_visited[idx+idy] = 1
                DFS(idy + 1)
                x_visited[idx] = 0
                right_down_visited[idx-idy] = 0
                right_up_visited[idx+idy] = 0

N = int(input())
x_visited = [0] * N
right_up_visited = [0] * (2 * N -1)
right_down_visited = [0] * (2 * N -1)

count = 0
DFS(0)
print(count)