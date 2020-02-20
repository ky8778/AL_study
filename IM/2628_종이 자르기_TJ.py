wid, hei = map(int, input().split())
cut_num = int(input())
kinds = []

for i in range(cut_num):
    kind = list(map(int, input().split()))
    kinds.append(kind)

total = [[None for _ in range(wid + 1)] for _ in range(hei + 1)]
x = [0, wid]
y = [0, hei]
for i in kinds:
    if i[0] == 0:
        y.append(i[1])
    elif i[0] == 1:
        x.append(i[1])
x.sort()
y.sort()
area = 0

for i in range(1, len(x)):
    for j in range(1, len(y)):
        if area < (x[i] - x[i-1]) * (y[j] - y[j-1]):
            area = (x[i] - x[i-1]) * (y[j] - y[j-1])
print(area)