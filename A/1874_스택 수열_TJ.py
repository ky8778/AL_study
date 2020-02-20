n = int(input())
sequence = [int(input()) for _ in range(n)]
stack = []
nums = [i for i in range(1, n+1)]
result = []
cnt = 0
while sequence:
    if nums:
        stack.append(nums.pop(0))
        result.append('+')
        while len(stack) != 0 and stack[-1] == sequence[0]:
            stack.pop()
            sequence.pop(0)
            result.append('-')
    else:
        if len(stack) != 0 and stack[-1] == sequence[0]:
            stack.pop()
            sequence.pop(0)
            result.append('-')
        else:
            result = ['NO']
            break
for R in result:
    print(R)