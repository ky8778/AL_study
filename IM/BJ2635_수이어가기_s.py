first = int(input())
num_list = []
num_length = 0
for second in range(1, first+1):
    new = 0
    numbers = []
    numbers.append(first)
    numbers.append(second)
    while new >= 0:
        new = numbers[-2] - numbers[-1]
        numbers.append(new)
    if numbers[-1] < 0:
        del numbers[-1]
    if num_length < len(numbers):
        num_length = len(numbers)
        num_list = numbers
print(num_length)
print(*num_list)    # * 언패킹