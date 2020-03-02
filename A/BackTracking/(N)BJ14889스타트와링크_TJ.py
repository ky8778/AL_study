def getresult(s,l):
    start = 0
    for y in range(len(s)):
        for x in range(y + 1,len(s)):
            start += S[s[y]][s[x]] + S[s[x]][s[y]]
            
    link = 0
    for y in range(len(s)):
        for x in range(y + 1,len(s)):
            link += S[s[y]][s[x]] + S[s[x]][s[y]]
    
    return abs(start-link)



def startlink(n):
    if n == N//2:
        global min_ans
        result = getresult(start,link)
        if min_ans > result:
            min_ans = result
    else:
        for y in range(N):
            if not visited[y]:
                visited[y] = 1
                start.append(y)
                link.remove(y)
                startlink(n + 1)
                visited[y] = 0
                start.remove(y)
                link.append(y)


N = int(input())
S = [list(map(int,input().split()))for _ in range(N)]
min_ans = 10000
visited = [0] * N
start = []
link = [n for n in range(N)]
startlink(0)
print(min_ans)