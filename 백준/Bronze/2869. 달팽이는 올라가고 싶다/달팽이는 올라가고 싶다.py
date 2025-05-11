A, B, V = input().split()

A = int(A)
B = int(B)
V = int(V)

if V == A:
    print(1)
elif (V - A) // (A - B) == 0:
    print(2)
else:
    if (V - A) // (A - B) * (A - B) + A >= V:
        print((V - A) // (A - B) + 1)
    else:
        print((V - A) // (A - B) + 2)

