def Devil(D, n, cnt, x):
    while n != cnt:
        x += 1
        if str(D) in str(x):
            cnt += 1
    return x


N = int(input())
Devil_num = 666
print(Devil(Devil_num, N, 0, 1))