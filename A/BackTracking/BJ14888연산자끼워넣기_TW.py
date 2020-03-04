'''
import sys
sys.stdin = open('14888.txt')
'''
Oper = ['+', '-', '*', '/']


def CALC(n1, n2, op) :
    if op == '+' : return n1 + n2
    elif op == '-' : return n1 - n2
    elif op == '*' : return n1 * n2
    else :
        if n1 > 0 and n2 > 0 : return n1 // n2
        else : return -(abs(n1) // abs(n2))


def GET() :
    global maxx, minn

    Ans = Arr[:]
    for i in range(N-1) :
        n1 = Ans.pop(0)
        n2 = Ans.pop(0)
        Ans.insert(0, CALC(n1, n2, Stack[i]))

    if Ans[0] > maxx : maxx = Ans[0]
    if Ans[0] < minn : minn = Ans[0]


def PERMUTE() :
    if len(Stack) == N-1 : 
        print(Stack)
        GET()
        return

    for i in range(4):
        if Oper_N[i] :
            Stack.append(Oper[i])
            Oper_N[i] -= 1

            PERMUTE()

            Stack.pop()
            Oper_N[i] += 1
    print

N = int(input())

Arr = list(map(int, input().split()))
Oper_N = list(map(int, input().split()))

Stack = []

minn = 1000000000
maxx = -1000000000

PERMUTE()

print(maxx)
print(minn)