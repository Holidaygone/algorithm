def is_promising(x):
    for a in range(x):
        if row[x] == row[a] or abs(row[x] - row[a]) == abs(x - a):
            return False
    return True

def n_queen(x):
    global result

    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i
            if is_promising(x):
                n_queen(x+1)

N = int(input())

result = 0

row = [0] * N

n_queen(0)

print(result)
