K=int(input())
stack=[]
for _ in range(K):
    t=int(input())
    if t!=0:
        stack.append(t)
    else:
        stack.pop()
print(sum(stack))