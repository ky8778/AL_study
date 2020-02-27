user_input = input()

N, M = map(int, user_input.split(' '))
numbers = list(range(1, N + 1))

def track(depth, ans):
    if depth == M:
        result = list(map(str, ans))

        print(' '.join(result))
        return
    for number in numbers:
        ans.append(number)
        track(depth + 1, ans)
        ans.pop()
track(0,[])