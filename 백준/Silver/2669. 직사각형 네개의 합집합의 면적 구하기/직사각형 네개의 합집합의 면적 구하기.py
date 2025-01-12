
list_map = [[0 for x in range(101)] for y in range(101)]

for i in range(4):

    x1, y1, x2, y2 = map(int, input().split())

    for a in range(x1, x2):
        for b in range(y1, y2):
            list_map[a][b] += 1

result = 0
for a in range(101):
    for b in range(101):
        if list_map[a][b] >= 1:
            result += 1

print(result)