def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

N = int(input())

switch_list = list(map(int, input().split()))

M = int(input())

student = []

for m in range(M):
    st = list(map(int, input().split()))
    student.append(st)

for i in range(M):
    gender = student[i][0]
    n = student[i][1]
    number = n - 1
    if gender == 1:
        while number < N:
            if switch_list[number] == 1:
                switch_list[number] = 0
            else:
                switch_list[number] = 1
            number += n
    if gender == 2:
        count = 0
        if switch_list[number] == 1:
            switch_list[number] = 0
        else:
            switch_list[number] = 1
        while True:
            count += 1
            if number + count < N and number - count >= 0 and \
                    switch_list[number + count] == switch_list[number - count]:
                if switch_list[number + count] == 1:
                    switch_list[number + count] = 0
                    switch_list[number - count] = 0
                else:
                    switch_list[number + count] = 1
                    switch_list[number - count] = 1
            else:
                break

for l in list_chunk(switch_list, 20):
    print(*l)



