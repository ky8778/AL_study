square_num = int(input())
square_dot = []
for i in range(square_num):
    length, height = map(int, input().split())
    square_dot.append([length, height])

total_area = [[0 for _ in range(101)] for _ in range(101)]
area = 0
for i in range(square_num):
    for y in range(101):
        for x in range(101):
            if square_dot[i][0] <= x < square_dot[i][0] + 10 and square_dot[i][1] <= y < square_dot[i][1] + 10:
                if total_area[y][x] == 0:
                    total_area[y][x] += 1
                    area += 1
print(area)