N = int(input())

sum = 0

for i in range(N // 2, N):

    sum += i
    
    str_i = str(i)
    
    for a in str_i:
        sum += int(a)
    
    if sum == N:
        print(i)
        break
    else: 
        sum = 0

if sum == 0:
    print(0)
