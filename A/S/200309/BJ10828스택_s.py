import sys
N = int(sys.stdin.readline())
stack = []
stack_len = 0

while N > 0:
    Input = sys.stdin.readline()
    N -= 1

    if 'push' in Input:
        stack_len += 1
        stack += [int(Input[5:])]

    elif 'pop' in Input:
        if stack:
            print(stack[-1])
            stack.pop()
            stack_len -= 1
        else:
            print(-1)

    elif 'size' in Input:
        print(stack_len)

    elif 'empty' in Input:
        if stack:
            print(0)
        else:
            print(1)

    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)