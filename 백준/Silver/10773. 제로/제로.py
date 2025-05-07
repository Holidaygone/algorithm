number = []

K = int(input())

for i in range(K):
    
    N = int(input())

    if N == 0 and number:
        number.pop()
    else:
        number.append(N)


result = 0

for n in number:
    result += n

print(result)