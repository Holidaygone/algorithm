n = int(input())

Apoint = 100
Bpoint = 100

for i in range(n):
    
    a, b = map(int, input().split())

    if a > b:
        Bpoint -= a
    elif a < b:
        Apoint -= b
    else:
        continue

print(Apoint)
print(Bpoint)