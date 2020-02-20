tcase = int(input())
for tc in range(tcase):
    string=input()
    stack=[]
    anw='YES'
    for i in string:
        # if len(stack)==0:
        #     stack.append(i)
        if i=='(':
            stack.append(i)
        else:
            if len(stack)==0:
                anw='NO'
                break
            if stack[-1]=='(':
                stack.pop()
            else:
                anw='NO'
    if len(stack)!=0:
        anw='NO'
    print(anw)