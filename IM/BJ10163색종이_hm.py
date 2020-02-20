import sys
sys.stdin = open('백준_10163_색종이.txt','r')

N = int(input())
arr = [[0] *101 for _ in range(101)]
# print(arr)
for i in range(1,N+1):
    point = list(map(int,input().split()))
    for j in range(point[0],point[0]+point[2]):
        for k in range(point[1],point[1]+point[3]):
            arr[j][k] = i
# print(arr)
for i in range(1,N+1):
    cnt = 0
    for j in range(101):
        cnt += arr[j].count(i)
    print(cnt)