N, M = map(int, input().split())

V = [0] * (N + 1)
Stack = []

def PERMUTE():
    if len(Stack) == M:
        print(*Stack)
        return

    for i in range(1, N + 1):
        if not V[i] :
            if not Stack or Stack[-1] < i :
                Stack.append(i)
                V[i] = 1
                PERMUTE()
                Stack.pop()
                V[i] = 0

PERMUTE()