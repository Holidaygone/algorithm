import math

N = int(input())

N_factorial = math.factorial(N)

Str_N = str(N_factorial)

count = 0

for i in Str_N[::-1]:
    if i == '0':
        count += 1
    else:
        break

print(count)