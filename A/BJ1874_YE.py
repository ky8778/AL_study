#스택 수열
n=int(input())
anwlist=[int(input()) for _ in range(n)]
tlist=list(range(2,n+1))
stack=[1]
i=j=0
alist=['+']
anw=True

while j<len(anwlist):
    goal=anwlist[j]
    if len(stack)==0 and i<anwlist[j]:
        stack.append(tlist[i])
        #print(stack)
        alist.append('+')
        #print(alist)
        i+=1

    if len(stack)!=0 and stack[-1]<goal:
        stack.append(tlist[i])
        #print(stack)
        alist.append('+')
        #print(alist)
        i+=1
    elif stack[-1]>goal:
        anw=False
        break

    elif stack[-1]==goal:
        stack.pop()
        #print(stack)
        alist.append('-')
        #print(alist)
        j+=1
    #print(j)
if anw==False:
    print('NO')
else:
    for i in alist:
        print(i)