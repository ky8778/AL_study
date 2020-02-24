#체스판 다시 칠하기
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
minn=987654321

for y in range(N-7):
    for x in range(M-7):
        for k in range(2):
            count=0
            for j in range(8):
                for i in range(8):
                    if k&1:
                        if (y+j)&1:
                            if (x+i)&1:
                                if arr[y+j][x+i]=='B':
                                    count+=1
                            else:
                                if arr[y+j][x+i]=='W':
                                    count+=1
                        else:
                            if (x+i)&1:
                                if arr[y+j][x+i]=='W':
                                    count+=1
                            else:
                                if arr[y+j][x+i]=='B':
                                    count+=1
                    else:
                        if (y+j)&1:
                            if (x+i)&1:
                                if arr[y+j][x+i]=='W':
                                    count+=1
                            else:
                                if arr[y+j][x+i]=='B':
                                    count+=1
                        else:
                            if (x+i)&1:
                                if arr[y+j][x+i]=='B':
                                    count+=1
                            else:
                                if arr[y+j][x+i]=='W':
                                    count+=1
            if count<minn:
                minn=count
print(minn)         