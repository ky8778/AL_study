length, height = map(int,input().split())
num = int(input())
Map = [[None for _ in range(length+1)] for _ in range(height+1)]

idx1, idx2 = 0, 0

for i in range(num):
    location, direction = map(int, input().split())
    if location == 1:
        Map[0][direction] = '*'
    elif location == 2:
        Map[height][direction] = '*'
    elif location == 3:
        Map[direction][0] = '*'
    elif location == 4:
        Map[direction][length] = '*'


location_man, direction_man = map(int, input().split())
if location_man == 1:
    idx1 = 0
    idx2 = direction_man
elif location_man == 2:
    idx1 = height
    idx2 = direction_man
elif location_man == 3:
    idx1 = direction_man
    idx2 = 0
elif location_man == 4:
    idx1 = direction_man
    idx2 = length

result = 0

for i in range(height + 1):
    for j in range(length + 1):
        if Map[i][j] == '*':
            if abs(i - idx1) == height:
                result += min(j + idx2 + height, length - j + length - idx2 + height)
            elif abs(j - idx2) == length:
                result += min(i + idx1 + length, height - i + height - idx1 + length)
            else:
                result += abs(i - idx1) + abs(j - idx2)
print(result)