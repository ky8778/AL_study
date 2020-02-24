T = int(input())

while T > 0:
    T -= 1
    TC = list(input())
    stack = 0

    for tc in TC:
        if stack < 0:
            break
        if tc == '(':
            stack += 1
        else:
            stack -= 1
    if stack:
        print('NO')
    else:
        print('YES')
