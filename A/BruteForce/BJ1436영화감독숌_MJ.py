N = int(input()) #N번째
i = 1
count = 0
while True:

    i += 1
    if '666' in str(i): #i에 666이 들어가면
        count += 1
    if count == N:
        print(i)
        break




