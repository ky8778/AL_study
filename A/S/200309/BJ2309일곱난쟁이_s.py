import copy
def FindReal(depth):
    global D_sum, Check, Result
    if depth == 7:
        if D_sum == 100:
            Result = copy.deepcopy(Real)
        return
    for i in range(9):
        if Check[i] == 0:
            Check[i] = 1
            Real.append(Dwarfs[i])
            D_sum += Dwarfs[i]
            FindReal(depth+1)
            Check[i] = 0
            Real.pop()
            D_sum -= Dwarfs[i]

Dwarfs = [int(input()) for _ in range(9)]
Check = [0]*9
Real = []
Result = []
D_sum = 0

FindReal(0)
Result.sort()
for i in range(7):
    print(Result[i])