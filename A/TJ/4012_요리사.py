import sys
sys.stdin = open('요리사.txt','r')


def getresult(s1,s2):
    global N
    hap1 = 0
    hap2 = 0
    for y in range(N//2):
        for x in range(y + 1, N//2):
            hap1 += S[s1[y]][s1[x]] + S[s1[x]][s1[y]]            
            hap2 += S[s2[y]][s2[x]] + S[s2[x]][s2[y]]
    
    return abs(hap1 - hap2)



def synergy(k,N,x,y):
    global min_num
    if k == N:
        result = getresult(s1,s2)
        if result < min_num:
            min_num = result
    else:
        if x < N//2:
            s1.append(k)
            synergy(k + 1, N, x + 1, y)
            s1.pop()

        if y < N//2:
            s2.append(k)
            synergy(k + 1, N, x, y + 1)
            s2.pop()




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    S = [list(map(int,input().split())) for _ in range(N)]
    min_num = 987654321
    s1 = []
    s2 = []
    synergy(0,N,0,0)
    print('#{} {}'.format(tc,min_num))