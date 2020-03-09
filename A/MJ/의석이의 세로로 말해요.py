T = int(input())

for tc in range(1, T+1):
    arr = []
    result=[]
    for i in range(5):
        str_arr = str(input()+'#################')
        arr.append(str_arr)
    for a in range(15):
        for b in range(5):
            if arr[b][a] != '#':
                result.append(arr[b][a])
    print('#%d ' %(tc) + ''.join(result))

    # max_len = 0
    # for l in range(5):
    #     if len(arr[i]) > max_len:
    #         max_len = len(arr[i])
    #
    # for k in range(max_len):
    #     for j in range(5):
    #         if arr[j][k]
    #         arr_1.append(arr[j][k])


# k가 max_len보다 작으면 ''를 append
# else : arr_1.append(arr[j][k])
