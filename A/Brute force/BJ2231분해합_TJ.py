N = int(input())
result = 1000000
for num in range(1,N):
    unit = []
    n = num
    while n:
        unit.append(n%10)
        n //= 10
    hap = sum(unit) + num
    if hap == N and result > num:
        result = num

if result == 1000000:
    print(0)
else:
    print(result)
