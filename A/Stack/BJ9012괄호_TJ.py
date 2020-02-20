def isvps(vps):
    if vps[0] == ')':
        return 'NO'
    else:
        for c in range(len(vps)):
            if vps[c] == '(':
                stack.append(vps[c])
            elif vps[c] == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return 'NO'
        if stack:
            return 'NO'
        else:
            return 'YES'

T = int(input())
for i in range(T):
    VPS = input()
    stack = []
    print(isvps(VPS))