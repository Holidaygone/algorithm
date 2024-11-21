N = int(input())

arr = list(map(int, input().split()))

result_count = 0

count = 1

n = 0
if N != 1:
    while n < N - 1:
        if arr[n] <= arr[n + 1]:
            while n < N - 1 and arr[n] <= arr[n + 1]:
                count += 1
                n += 1
        if result_count < count:
            result_count = count
        n += 1
        count = 1
    n = 0
    count = 1
    while n < N - 1:
        if arr[n] >= arr[n + 1]:
            while n < N - 1 and arr[n] >= arr[n + 1]:
                count += 1
                n += 1
        if result_count < count:
            result_count = count
        n += 1
        count = 1
else:
    result_count = 1


print(result_count)
