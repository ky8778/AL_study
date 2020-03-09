#! 2020.03.06
# TODO SWEA1249_보급로
#! BFS Algorithm
import sys
sys.stdin = open('input.txt', 'r')
import queue
T = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
INF = float('inf')

def inRange(y,x):
    if y>=0 and y<N and x>=0 and x<N:
        return True
    else:
        return False

def isEnd(y,x):
    if y==N-1 and x==N-1:
        return True
    else:
        return False

def getResult():
    myQ = queue.Queue()
    myQ.put([0,0])
    dist[0][0] = 0

    while not myQ.empty():
        now = myQ.get()
        for dir in range(4):
            next = [now[0]+dx[dir],now[1]+dy[dir]]
            if inRange(next[0],next[1]):
                nextDist = dist[now[0]][now[1]]+inData[next[0]][next[1]]
                if dist[next[0]][next[1]] > nextDist:
                    dist[next[0]][next[1]] = nextDist
                    myQ.put(next)
    return dist[N-1][N-1]

for tc in range(1,T+1):
    N = int(input())
    inData = [list(map(int,input())) for _ in range(N)]
    dist = [[INF for _ in range(N)] for _ in range(N)]
    print("#{0} {1}".format(tc,getResult()))