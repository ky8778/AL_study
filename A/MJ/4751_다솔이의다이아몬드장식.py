T = int(input())

for tc in range(1, T+1):
    N = input()
    result3 = '.#.'.join(N)
    result3_1 = '#.' + result3 + '.#'
    result2 = ['']*len(result3_1)
    result1 = []
    for i in range(len(result3_1)):
        if i%2 == 1:
            result2[i] = '#'
        else:
            result2[i] = '.'
    result2 = ''.join(result2)
    for j in range(len(result3_1)):
        if j%4 == 2:
            result1.append('#')
        else:
            result1.append('.')
    result1 = ''.join(result1)

    print(result1)
    print(result2)
    print(result3_1)
    print(result2)
    print(result1)