#스타트와 링크
def Score(team):
    r = 0
    for i in team:
        for j in team:
            #if i!=j:
            r+=arr[i][j]
    return r

def MakeTeam(idx): 
    global teamB, anw, minn
    if len(teamA)==N//2:
        for k in range(N):
            if not visited[k]:
                teamB.append(k)

        result = abs(Score(teamA) - Score(teamB))

        if result == 0:
            anw = True
            minn = result
            return

        elif result < minn: 
            minn=result
        teamB = []
        return

    for t in range(idx,N):
        if not visited[t]:
            visited[t]=True
            teamA.append(t)

            MakeTeam(t)

            if anw:
                break
            visited[t]=False
            teamA.pop()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited=[False for _ in range(N)]
teamA = []
teamB = []
anw = False
minn=987654321

MakeTeam(0)
print(minn)