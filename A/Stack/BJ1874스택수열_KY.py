#! 2020.02.19
# TODO BJ1874_스택수열
N = int(input())
myStack = []
top = -1
wantMake = []
result = []

for i in range(1,N+1):
    tmp = int(input())
    wantMake.append(tmp)

idx = 0

for i in range(1,N+1):
    top+=1
    myStack.append(i)
    result.append('+')
    while top >= 0 and myStack[top] == wantMake[idx]:
        top -= 1
        idx += 1
        myStack.pop()
        result.append('-')

if len(myStack)<=0:
    for i in result:
        print(i)
else:
    print("NO")