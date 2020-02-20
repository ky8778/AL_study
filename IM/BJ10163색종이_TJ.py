pieces = int(input())
cnt = [0 for _ in range(pieces + 1)]
square = [[0 for _ in range(101)] for _ in range(101)]

for i in range(1, pieces + 1):
    Square = list(map(int,input().split()))
    for y in range(Square[1], Square[1] + Square[3]):
        for x in range(Square[0], Square[0] + Square[2]):
            square[y][x] = i

for i in range(1, pieces + 1):
    for y in range(101):
        for x in range(101):
            if square[y][x] == i:
                cnt[i] += 1
    print(cnt[i])