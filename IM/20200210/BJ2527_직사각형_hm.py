import sys
sys.stdin = open('백준_2527_직사각형.txt','r')

for i in range(4):
    data = list(map(int,input().split()))
    # print(data)

    if data[3] < data[5] or data[2] < data[4] or data[7] < data[1] or data[6] < data[0]:
        print('d')
    elif (data[4] == data[2] and data[5] == data[3]) or (data[5] == data[3] and data[0] == data[6]) or (data[0] == data[6] and data[1] == data[7]) or (data[1] == data[7] and data[4] == data[2]):
        print('c')
    elif (data[4] == data[2] and data[5] < data[3]) or (data[5] == data[3] and data[4] < data[2]) or (data[0] == data[6] and data[1] < data[7]) or (data[1] == data[7] and data[0] < data[6]):
        print('b')
    else:
        print('a')