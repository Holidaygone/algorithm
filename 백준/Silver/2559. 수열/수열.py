import sys

input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))

hap = sum(arr[:K])

max_hap = hap
count = 0
for i in range(K, N):
    hap = hap + arr[K + count] - arr[i - K]
    count += 1
    if max_hap < hap:
        max_hap = hap
print(max_hap)
