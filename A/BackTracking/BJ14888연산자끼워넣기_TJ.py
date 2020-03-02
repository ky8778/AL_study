def calculation(n, k, result, add, subtraction, multiply, division):
    global max_ans, min_ans
    if n == k:
        if max_ans < result:
            max_ans = result
        if min_ans > result:
            min_ans = result
        return
    else:
        if add > 0:
            calculation(n + 1, k, result + card[n], add - 1, subtraction, multiply, division)
        if subtraction > 0:
            calculation(n + 1, k, result - card[n], add, subtraction - 1, multiply, division)
        if multiply > 0:
            calculation(n + 1, k, result * card[n], add, subtraction, multiply - 1, division)
        if division > 0:
            if result < 0 and card[n] > 0 or result > 0 and card[n] < 0:
                calculation(n + 1, k, (-1)*(abs(result) // abs(card[n])), add, subtraction, multiply, division - 1)
            else:
                calculation(n + 1, k, result // card[n], add, subtraction, multiply, division - 1)


N = int(input())
card = list(map(int,input().split()))
add, subtraction, multiply, division = map(int,input().split())
max_ans = -1000000000
min_ans = 1000000000
calculation(1, N, card[0], add, subtraction, multiply, division)
print(max_ans)
print(min_ans)