N, M = map(int, input().split())
card_list = list(map(int, input().split()))
result = 0
for z in card_list:
    first = z
    for y in card_list:
        if y != first:
            second = y
            for x in card_list:
                if x != first and x != second:
                    third = x
                    hap = z + y + x
                    if result < hap <= M:
                        result = hap
print(result)