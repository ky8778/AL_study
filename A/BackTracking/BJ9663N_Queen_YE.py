#N-Queen
def isSafe(nextx, tempy):
    for t in range(len(qlist)):
        if nextx in qlist or abs(nextx-qlist[t]) == tempy - t :
            return False
    return True

def nQueen(tempy):
    global count

    if tempy==N:
        count+=1
        return
    
    for x in range(N):
        if isSafe(x,tempy):
            qlist.append(x)
            nQueen(tempy+1)
            qlist.pop()
            
N = int(input())
qlist = []
count = 0

nQueen(0)
print(count)