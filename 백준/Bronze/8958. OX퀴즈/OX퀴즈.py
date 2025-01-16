T = int(input())
for i in range(T):
    str_input = input()
    cnt = 0
    point = 0
    for j in range(len(str_input)):
        if str_input[j] == 'O':
            cnt += 1
            point += cnt
        else:
            cnt = 0
    print(point)