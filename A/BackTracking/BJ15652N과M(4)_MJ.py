user_input = input()

N, M = map(int, user_input.split())
numbers = list(range(1, N + 1))

def track(depth, ans):
    if depth == M:
        # result = ans[:]
        # for i in range(M-1):
        #     if result[i] > result[i+1]:
        #         break
        # else:
        #     print(*result)
        for i in range(M-1):
            if ans[i] > ans[i+1]:
                break
            else:
                print(*ans)
        return
    for number in numbers:
        ans.append(number)
        track(depth + 1, ans)
        ans.pop()
track(0,[])