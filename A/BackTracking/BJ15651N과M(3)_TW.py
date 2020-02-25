N, M = map(int, input().split())

Stack = []


def PERMUTE():
    if len(Stack) == M:
        print(*Stack)
        return

    for i in range(1, N + 1):
        Stack.append(i)
        PERMUTE()
        Stack.pop()


PERMUTE()