C, R = map(int, input().split())

K = int(input())

seat = []

for j in range(R, 0, -1):
    seat_1 = []
    for i in range(1, C + 1):
        seat_1.append((i, j))
    seat.append(seat_1)

seat_check = [[False for _ in range(C)] for _ in range(R)]

seat_number = [[0 for _ in range(C)] for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

a = R - 1
b = 0
status = True
count = 0
line_change = False
while status:
    status = False

    for i in range(4):
        if line_change:
            a = a + dx[i]
            b = b + dy[i]

        # print('a, b, i', a, b, i)

        while 0 <= a < R and 0 <= b < C and seat_check[a][b] == False:
            count += 1
            status = True
            seat_number[a][b] = count
            seat_check[a][b] = True
            if 0 <= a + dx[i] < R and 0 <= b + dy[i] < C and seat_check[a + dx[i]][b + dy[i]] == False:
                a = a + dx[i]
                b = b + dy[i]

        line_change = True

    for j in range(4):
        a1 = a + dx[j]
        b1 = b + dy[j]
        if 0 <= a1 < R and 0 <= b1 < C and seat_check[a1][b1] == False:
            status = True
    # print(status)

# print(seat_number)
result = 0
for i in range(R):
    for j in range(C):
        if seat_number[i][j] == K:
            result = seat[i][j]
try:
    print(*result)
except:
    print(0)