from itertools import combinations

N, M = map(int, input().split())

number_list = list(map(int, input().split()))

result = 0
for i in combinations(number_list, 3):
    hap = 0
    for j in i:
        hap += j
    if result == 0 and hap <= M:
        result = hap
    elif result < hap <= M:
        result = hap

print(result)
