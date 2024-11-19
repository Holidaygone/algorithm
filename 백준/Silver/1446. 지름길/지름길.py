def dfs(n, m, i):
    global result
    # n 은 현재 위치 m 은 달린 거리 i 는 인덱스
    #print(n, m, i)

    if n == D:
        if result > m:
            result = m
        return
    if i < N1:
        if n == way[i][0]:
            dfs(way[i][1], m + way[i][2], i + 1)
            dfs(n, m, i + 1)
        elif n < way[i][0]:
            dfs(way[i][1], m + way[i][2] + way[i][0] - n, i + 1)
            dfs(n, m, i + 1)
        elif n > way[i][0]:
            dfs(n, m, i + 1)
    else:
        m = m + (D - n)
        if result > m:
            result = m
        return


N, D = map(int, input().split())

way = []
N1 = 0
for i in range(N):
    arr = list(map(int, input().split()))
    if arr[1] <= D and arr[1] - arr[0] > arr[2]:
        way.append(arr)
        N1 += 1
#print('N1', N1)
way.sort()
#print(way)
result = D

dfs(0, 0, 0)

print(result)