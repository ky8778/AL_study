#! 2020.02.19
# TODO BJ4949_균형잡힌세상

inData = input()
myStack = None
top = None

def initStack():
    global myStack,top
    top = -1
    myStack = []

def getResult(inStr):
    global top
    for i in inStr:
        if i=='(' or i=='[':
            myStack.append(i)
            top+=1
        elif i==')':
            if top<0:
                return "no"
            else:
                check = myStack.pop()
                top-=1
                if check!='(':
                    return "no"
        elif i==']':
            if top<0:
                return "no"
            else:
                check = myStack.pop()
                top-=1
                if check!='[':
                    return "no"
    if top>=0:
        return "no"
    else:
        return "yes"

while len(inData)>1:
    initStack()
    print(getResult(inData))
    inData = input()