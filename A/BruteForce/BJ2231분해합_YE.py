#분해합
N = int(input())
lenN=len(str(N))

temp = N - 9*lenN
if temp < 0:
    temp = 0

while True:
    tsum=temp
    for i in str(temp):
        tsum+=int(i)
    
    if temp > N:
        print (0)
        break
    elif tsum != N:
        temp += 1
    elif tsum == N:
        print(temp)
        break