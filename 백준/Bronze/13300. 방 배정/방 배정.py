
N, K = map(int, input().split())

dict_student = {}

for i in range(2):
    for j in range(1, 7):
        ij = str(i) + str(j)
        dict_student[ij] = 0

for n in range(N):
    i, j = map(str, input().split())
    ij = i + j
    dict_student[ij] += 1

result = 0


for i in range(2):
    for j in range(1, 7):
        ij = str(i) + str(j)
        if dict_student[ij] == 0:
            continue
        elif dict_student[ij] % K == 0:
            result += int(dict_student[ij] / K)
        elif dict_student[ij] % K != 0:
            result += dict_student[ij] // K + 1


print(result)