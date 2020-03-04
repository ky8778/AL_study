import queue
N,M,V = map(int,input().split())
myMap = [[] for _ in range(N+1)]

def DFS(now):
    print(now,end=' ')
    
    for next in myMap[now]:
        if not checkMap[next]:
            checkMap[next] = True
            DFS(next)

def BFS(now):
    checkMap[now] = True
    myQ.put(now)

    while not myQ.empty():
        current = myQ.get()
        print(current,end=' ')
        for next in myMap[current]:
            if not checkMap[next]:
                checkMap[next] = True
                myQ.put(next)

for i in range(M):
    start, end = map(int,input().split())
    myMap[start].append(end)
    myMap[end].append(start)

for i in range(N+1):
    myMap[i].sort()

checkMap = [False for _ in range(N+1)]
checkMap[V] = True
DFS(V)
print()

checkMap = [False for _ in range(N+1)]
myQ = queue.Queue()
BFS(V)
print()