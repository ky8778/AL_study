# N = int(input())



def SIX(Temp) :
    Stack = []

    for i in Temp :
        if i == 6 and not Stack : Stack.append(i)
        elif i != 6 and Stack : Stack.clear()
        elif i == 6 and Stack : Stack.append(i)

        if len(Stack) >= 3 : return True
    return False

N = 10
cnt = 0
i = 666
now = i

while True :
    if cnt == N :
        print(now)
        break

    Temp = list(map(int, str(i)))

    if SIX(Temp) :
        cnt += 1
        now = i

    i += 1