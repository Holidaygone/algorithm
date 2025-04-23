T = int(input())

for i in range(T):
    N = int(input())
    sum_C = 0
    avg_G = 0
    for j in range(N):
        C_str, G_str = input().split()
        C = int(C_str)
        G = float(G_str)
        sum_C += C
        avg_G += C * G
    avg_G = avg_G / sum_C

    print(sum_C, round(avg_G + 1e-8, 1))