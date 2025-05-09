import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):

    order = sys.stdin.readline().split()

    if len(order) == 1:
        command = int(order[0])
    elif len(order) == 2:
        command = int(order[0])
        number = int(order[1])

    if command == 1:
        stack.append(number)
    elif command == 2:
        if not stack:
            print(-1)
        else:
            pop_number = stack.pop()
            print(pop_number)
    elif command == 3:
        print(len(stack))
    elif command == 4:
        if not stack:
            print(1)
        else:
            print(0)
    elif command == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)        