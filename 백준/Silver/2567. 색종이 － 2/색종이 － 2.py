
area = [[0 for _ in range(102)] for _ in range(102)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
# 색종이의 가로 세로는 10, 색종이 개수 100개 이하
for n in range(N):
    x, y = map(int, input().split())

    for i in range(10):
        for j in range(10):
            area[x+i][y+j] = 1
length = 0
for i in range(101):
    for j in range(101):
        if area[i][j] == 1:
            for k in range(4):
                di = i + dx[k]
                dj = j + dy[k]

                if area[di][dj] == 0:
                    length += 1

print(length)