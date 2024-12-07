N = int(input())
# 6, 12, 18
n = 1
m = 1
while N > m:
    m += 6 * n
    n += 1

print(n)