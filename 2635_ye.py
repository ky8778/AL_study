first = int(input())
anw=0
anwtemp=[]

for n in range(1,first+1):
    temp=[first,n]

    while True:
        if temp[-1]<0:
            temp=temp[:-1]
            break
        temp.append(temp[-2]-temp[-1])

    if anw > len(temp):

        break
    else:
        anw=len(temp)
        anwtemp=temp

print(anw)
print(*anwtemp)