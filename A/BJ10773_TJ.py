num = int(input())
stack = []
for i in range(num):
    money = int(input())
    if money != 0:
        stack.append(money)
    elif money == 0:
        stack.pop()
print(sum(stack))