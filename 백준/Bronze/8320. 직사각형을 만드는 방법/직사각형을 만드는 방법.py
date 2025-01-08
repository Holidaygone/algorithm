def get_divisor(n):
    d_list = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            d_list.append(i)
    return len(d_list)


n = int(input())

count = 0
for i in range(1, n + 1):
    count += get_divisor(i)

print(count)
