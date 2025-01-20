N = int(input())

A = list(map(int, input().split()))

M = int(input())

M_list = list(map(int, input().split()))
A1 = []
for m in M_list:
    if m in A1:
        print(1)
    elif m in A:
        print(1)
        A1.append(m)
    else:
        print(0)