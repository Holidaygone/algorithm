
list_map = [[0 for x in range(1001)] for y in range(1001)]

N = int(input())

paper = 1

min_x = 0
max_x = 0
min_y = 0
max_y = 0
min_x_check = 0
min_y_check = 0
max_x_check = 0
max_y_check = 0

for i in range(N):

    x, y, w, h = map(int, input().split())

    for a in range(x, x + w):
        for b in range(y, y + h):
            list_map[a][b] = paper
    paper += 1

    if min_x_check == 0:
        min_x = x
        min_x_check += 1
    elif min_x > x:
        min_x = x
    if max_x_check == 0:
        max_x = x+w
        max_x_check += 1
    elif max_x < x+w:
        max_x = x+w
    if min_y_check == 0:
        min_y = y
        min_y_check += 1
    elif min_y > y:
        min_y = y
    if max_y_check == 0:
        max_y = y+h
        max_y_check += 1
    elif max_y < y+h:
        max_y = y + h

paper = 1
for i in range(N):
    cnt = 0
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if list_map[x][y] == paper:
                cnt += 1
    print(cnt)
    paper += 1
