#! 2020.03.06
# TODO SWEA1249_보급로
'''
import sys
sys.stdin = open('input.txt', 'r')

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
    while True:
        minDist = INF
        for now in mynodes:    
            # print(now)
            for dir in range(4):
                nextY = now[0]+dy[dir]
                nextX = now[1]+dx[dir]
                if inRange(nextY,nextX) and not checkMap[nextY][nextX]:
                    dist[nextY][nextX] = min(dist[now[0]][now[1]]+inData[nextY][nextX],dist[nextY][nextX])
                    if minDist > dist[nextY][nextX]:
                        minDist = dist[nextY][nextX]
                        minNextY, minNextX = nextY, nextX

        # print(minNextY,minNextX)
        # print(mynodes)
        mynodes.append([minNextY,minNextX])
        checkMap[minNextY][minNextX] = True
        if isEnd(minNextY,minNextX):
            break

    return dist[N-1][N-1]

for tc in range(1,T+1):
    N = int(input())
    inData = [list(map(int,input())) for _ in range(N)]
    dist = [[INF for _ in range(N)] for _ in range(N)]
    checkMap = [[False for _ in range(N)] for _ in range(N)]
    dist[0][0] = 0
    checkMap[0][0] = True
    mynodes = []
    mynodes.append([0,0])
    print("#{0} {1}".format(tc,getResult()))

'''


import sys
sys.stdin = open('input.txt', 'r')
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

def getResult(yy,xx,sumPrice):
    stack = []
    stack.append([0,0,0])
    top = 0
    checkMap[0][0] = True
    while stack:
        now = stack[top]
        cnt = 0
        for dir in range(4):
            nextY = now[0] + dy[dir]
            nextX = now[1] + dx[dir]
            if inRange(nextY,nextX) and not checkMap[nextY][nextX]:
                price = now[2]+inData[nextY][nextX]
                if price < DP[nextY][nextX] and price < DP[N-1][N-1]:
                    top+=1
                    stack.append([nextY,nextX,price])
                    DP[nextY][nextX] = price
                    checkMap[nextY][nextX] = True
                    cnt+=1
        
        if cnt==0:
            stack.pop()
            checkMap[now[0]][now[1]] = False
            top-=1
            
    return DP[N-1][N-1]
                

for tc in range(1,T+1):
    N = int(input())
    inData = [list(map(int,input())) for _ in range(N)]
    DP = [[INF for _ in range(N)] for _ in range(N)]
    checkMap = [[False for _ in range(N)] for _ in range(N)]
    print("#{0} {1}".format(tc,getResult(0,0,0)))