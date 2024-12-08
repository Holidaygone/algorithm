A, B, C = map(int, input().split())

if B < C:

    cnt = int(A / (C-B)) + 1

    print(cnt)
    
elif B >= C:
    print(-1)