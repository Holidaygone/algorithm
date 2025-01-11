K = int(input())

list1 = []
for i in range(6):
    x, y = map(int, input().split())
    list1.append([x, y])
max_n = 0
max_idx = 0
for idx, n in enumerate(list1):
    #print(idx, n)
    if max_n < n[1]:
        max_n = n[1]
        max_idx = idx
#print('max_idx', max_idx, 'max_n', max_n)
list2 = [[0, 0] for _ in range(6)]
for idx, n in enumerate(list1):
    if idx < max_idx:
        idx_1 = 5 - max_idx + idx + 1
        list2[idx_1] = n
    elif idx == max_idx:
        idx_1 = 0
        list2[idx_1] = n
    elif idx > max_idx:
        idx_1 = idx - max_idx
        list2[idx_1] = n
#print(list2)

n = []
wide = []
height = []
count1 = 0
count2 = 0
count3 = 0
count4 = 0
n_cnt = 0
status = True
for i in range(6):
    x, y = list2[i]
    if x == 1:
        count1 += 1
        n.append(y)
        wide.append(y)
        n_cnt += 1

    elif x == 2:
        count2 += 1
        n.append(y)
        wide.append(y)
        n_cnt += 1

    elif x == 3:
        count3 += 1
        n.append(y)
        height.append(y)
        n_cnt += 1

    elif x == 4:
        count4 += 1
        n.append(y)
        height.append(y)
        n_cnt += 1

    if count1 == 2 or count2 == 2 or count3 == 2 or count4 == 2:
        if status:
            minus_a = y
            minus_b = n[n_cnt - 2]
            status = False
            #print('minus', minus_a, minus_b, status)

total = max(wide) * max(height)
#print('total', total)
result = total - (minus_a * minus_b)

print(result*K)