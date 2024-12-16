N = int(input())

list_map = [[0 for x in range(101)] for y in range(101)]

min_x = 0
max_x = 0
min_y = 0
max_y = 0
min_x_check = 0
min_y_check = 0
max_x_check = 0
max_y_check = 0

for i in range(N):

    x, y = map(int, input().split())

    for a in range(x, x + 10):
        for b in range(y, y + 10):
            list_map[a][b] += 1

    if min_x_check == 0:
        min_x = x
        min_x_check += 1
    elif min_x > x:
        min_x = x
    if max_x_check == 0:
        max_x = x+10
        max_x_check += 1
    elif max_x < x+10:
        max_x = x+10
    if min_y_check == 0:
        min_y = y
        min_y_check += 1
    elif min_y > y:
        min_y = y
    if max_y_check == 0:
        max_y = y+10
        max_y_check += 1
    elif max_y < y+10:
        max_y = y + 10

area = 0
for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        if list_map[x][y] >= 1:
            area += 1
print(area)
