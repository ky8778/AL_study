#균형잡힌 세상
string=input()
while string!='.':
    stack=[]
    anw='yes'
    for n in string:
        if n=='(' or n=='[':
            stack.append(n)
        elif n==')':
            if len(stack)==0:
                anw='no'
                continue
            if stack[-1]=='(':
                stack.pop()
            else: 
                anw='no'
                continue
        elif n==']':
            if len(stack)==0:
                anw='no'
                continue
            if stack[-1]=='[':
                stack.pop()
            else: 
                anw='no'
                continue

    if len(stack)!=0:
        anw='no'

    print(anw)
    string = input()