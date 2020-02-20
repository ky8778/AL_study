def isstring(string,cnt):
    if string[0] == ']' or string[0] == ')':
        return 'no'
    else:
        while cnt < len(string):
            if string[cnt] == '[' or string[cnt] == '(':
                stack.append(string[cnt])
            elif len(stack) != 0 and string[cnt] == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return 'no'
            elif len(stack) != 0 and string[cnt] == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return 'no'
            elif len(stack) == 0 and string[cnt] == ']' or string[cnt] == ')':
                return 'no'
            cnt += 1
        if stack:
            return 'no'
        else:
            return 'yes'


string = input()
while string != '.':
    stack = []
    print(isstring(string,0))
    string = input()