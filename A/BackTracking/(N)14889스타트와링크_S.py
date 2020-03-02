# 1. 팀을 A와 B로 나누고, A팀을 선발하면 나머지는 B팀이 되도록 설정
# 2. 먼저 A팀을 뽑을 수 있는 경우의 수를 확인한다.(def Maketeam())
# 3. 각 경우의 수가 나올 때마다 상황별로 상대팀(B팀)을 만들고 (def MakeB())
# 4. 만들어진 A팀과 B팀의 능력치를 각각 계산한다(Cal(team_A), Cal(team_B))
# 5. 능력치 차이의 최소값을 구한다.(Findmin())
# 6. 답을 출력한다.

# 재귀 안에서 함수를 호출하는 것 때문에 오래 걸리나?
# 근데 어떡해 다른 방법을 모르는데

def Maketeam(depth):
    global Case
    if depth == N/2:
        team_B = MakeB(team_A)
        Exp_A = Cal(team_A)
        Exp_B = Cal(team_B)
        Findmin(Exp_A, Exp_B)
        return
    for i in range(N):
        if i not in team_A:
            team_A.append(i)
            Maketeam(depth+1)
            team_A.pop()

def MakeB(lst):
    B = []
    for b in range(N):
        if b not in lst:
            B.append(b)
    return B

def Cal(lst):
    Exp = 0
    for e in range(len(lst)-1):
        for ee in range(e, len(lst)):
            Exp += S[lst[e]][lst[ee]]
            Exp += S[lst[ee]][lst[e]]
    return Exp

def Findmin(A, B):
    global min_gap
    gap = ((A-B)**2)**0.5
    if gap < min_gap:
        min_gap = gap
    return

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
Case = []
team_A = []
min_gap = 987654321

Maketeam(0)

print(int(min_gap))
