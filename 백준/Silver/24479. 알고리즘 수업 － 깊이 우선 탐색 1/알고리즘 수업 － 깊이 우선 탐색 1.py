def dfs(R):
    stack = []
    visited = [False] * (N + 1)
    global count
    cnt = 1
    stack.append(R)

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            count[v] = cnt
            cnt += 1
        for w in adjM[v]:
            if not visited[w]:
                stack.append(w)

    return


N, M, R = map(int, input().split())

adjM = [[] for _ in range(N + 1)]

for n in range(M):

    v1, v2 = map(int, input().split())

    adjM[v1].append(v2)
    adjM[v2].append(v1)

for x in range(1, N+1):
    adjM[x] = sorted(adjM[x], reverse=True)

count = [0] * (N + 1)

dfs(R)

for c in count[1:]:
    print(c)