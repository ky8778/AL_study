#빙고
bingo=[list(map(int, input().split())) for _ in range(5)]
mc=[]
for i in range(5):
    mc+=list(map(int, input().split()))

for k in range(25):
    for x in range(5):#숫자 찾아서 지우기
        for y in range(5):
            if mc[k]==bingo[y][x]:
                bingo[y][x]=0

    dcount=0
    ddcount=0
    count=0
    for i in range(5):
        zcount=0
        for j in range(5):
            if bingo[j][i]==0: #세로줄
                zcount+=1
        count+=zcount//5
        if bingo[i]==[0]*5: #가로줄
            count+=1
        if bingo[i][i]==0: #왼쪽 대각선
            dcount+=1
        if bingo[i][4-i]==0: #오른쪽 대각선
            ddcount+=1
    
    if count + (dcount//5) + (ddcount//5)>=3:
        print(k+1)
        break