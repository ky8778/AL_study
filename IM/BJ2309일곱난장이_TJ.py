small_list = []
for i in range(9):
    small = int(input())
    small_list.append(small)

result = 0
for i in range(1<<9):
    smalls = []
    for j in range(10):
        if i & (1<<j):
            smalls.append(small_list[j])
    if sum(smalls) == 100 and len(smalls) == 7:
        result = smalls

result.sort()
for i in result:
    print(i)