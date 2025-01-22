T = int(input())

for i in range(T):

    Ypoint = 0
    Kpoint = 0

    for j in range(9):
        Y, K = map(int, input().split())

        Ypoint += Y
        Kpoint += K

    if Ypoint > Kpoint:
        print("Yonsei")
    elif Ypoint == Kpoint:
        print("Draw")
    else:
        print("Korea")