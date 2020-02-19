#! 2020.02.18
# TODO BJ10773_제로

K = int(input())
myStack = []
top = -1

for k in range(K):
    num = int(input())
    if num!=0:
        myStack.append(num)
        top+=1
    else:
        if top>=0:
            myStack.pop()
            top-=1
    
result = 0
while top >= 0:
    result += myStack.pop()
    top-=1
print(result)