import sys

X = int(sys.stdin.readline())


low = 1
high = 50000
k = 0

while low <= high:
    mid = (low + high) // 2
    count = (mid * (mid + 1)) // 2
    
    if count >= X:
        k = mid
        high = mid - 1
    else:
        low = mid + 1

prev_count = ((k - 1) * k) // 2
order_in_group = X - prev_count

if (k + 1) % 2 == 0:
    print(f"{k + 1 - order_in_group}/{order_in_group}")
else:
    print(f"{order_in_group}/{k + 1 - order_in_group}")