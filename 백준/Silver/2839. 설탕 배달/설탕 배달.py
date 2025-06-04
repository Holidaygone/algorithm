N = int(input())

five_count = N // 5
left = N % 5
count = 0
while five_count >= 0:

    if left % 3 == 0:
        count = five_count + (left // 3)
        print(count)
        exit()
    five_count -= 1
    left += 5

print(-1)
