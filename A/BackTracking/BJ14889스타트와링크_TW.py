import sys
sys.stdin = open('14889.txt', 'r')

# 1. N명의 멤버들 가운데 N/2 명을 A팀으로 선발 (조합)
#    ex) N=6, A=[1,1,1,0,0,0]
#
# 2. 나머지를 B팀으로 선발
#    ex) N=6, B=[0,0,0,1,1,1]
#
# 3. 각 팀마다 2명씩 짝지어서 능력치 계산
# 4. 비교 후 출력


def TEAM_A(now) :
    global A, cnt, point, minn

    if cnt == N >> 1 : # N/2명 선택됐을 때
        B = TEAM_B()

        PAIR(A); point_A, point = point, 0
        PAIR(B); point_B, point = point, 0

        x = abs(point_A - point_B)
        if x < minn : minn = x
        return

    for i in range(now, N) : # N/2명 선택해서 A에 넣는 조합 // cnt : 현재까지 선택된 인원 수
            A[i] = 1
            cnt += 1
            TEAM_A(i+1)
            A[i] = 0
            cnt -= 1

# 팀 B를 어떻게 구하면 좋을까? --> A 복사해서 0, 1 반전
def TEAM_B() :
    B = A[:]
    for i in range(N) : B[i] = 1-B[i]
    return B

# 2명만큼 선택하는 순열 --> 2명 선택하는 조합 시도해봤지만 // 메모리, 시간은 오히려 늘어남??
def PAIR(Team) :
    global Stack, point
    if len(Stack) == 2 :
        point += CALC()
        return

    for i in range(N) :
        if Team[i] :
            Team[i] = 0
            Stack.append(i)
            PAIR(Team)
            Team[i] = 1
            Stack.pop()

def CALC() :
    global Stack
    return Arr[Stack[0]][Stack[1]]


N = int(input())
Arr = [list(map(int, input().split())) for _ in range(N)]
A = [0] * N
cnt, point, minn = 0, 0, 987654321
Stack = []

TEAM_A(0)

print(minn)