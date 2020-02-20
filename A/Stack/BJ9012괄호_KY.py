#! 2020.02.18
# TODO BJ9012_괄호
import string

T = int(input())
inData = None
myStack = None
top = None

def initStack():
    global top,myStack
    myStack = []
    top = -1

def getResult(inStr):
    global top
    for i in inStr:
        if i=='(':
            myStack.append(i)
            top+=1
        else:
            if top>=0:
                myStack.pop()
                top-=1
            else:
                return "NO"
    if top==-1:
        return "YES"
    else:
        return "NO"

for tc in range(1,T+1):
    inData = list(input())
    initStack()
    print(getResult(inData))    