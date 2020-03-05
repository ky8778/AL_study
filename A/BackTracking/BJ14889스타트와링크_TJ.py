def getresult(s,l):
    start = 0
    for y in range(len(s)):
        for x in range(y + 1,len(s)):
            start += S[s[y]][s[x]] + S[s[x]][s[y]]

    link = 0
    for y in range(len(s)):
        for x in range(y + 1,len(s)):
            link += S[l[y]][l[x]] + S[l[x]][l[y]]

    return abs(start-link)



def startlink(n,N):
    global min_ans
    if n == N:
        result = getresult(start,link)
        if min_ans > result:
            min_ans = result
    else:
        if len(start) < N//2:
            start.append(n)
            startlink(n + 1, N)
            start.pop()
        if len(link) < N // 2: 
            link.append(n)
            startlink(n + 1, N)
            link.pop()
            


N = int(input())
S = [list(map(int,input().split()))for _ in range(N)]
min_ans = 987654321
start = []
link = []
startlink(0,N)
print(min_ans)