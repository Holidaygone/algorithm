from queue import deque
import sys

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, x):
        self.queue.append(x)

    def pop(self):
        print(self.queue.popleft() if self.queue else -1)
    
    def size(self):
        print(len(self.queue))
    
    def empty(self):
        print(1 if not self.queue else 0)
    
    def front(self):
        print(self.queue[0] if self.queue else -1)
    
    def back(self):
        print(self.queue[-1] if self.queue else -1)

queue = Queue()

n = int(sys.stdin.readline().strip())


for _ in range(n):
    command = sys.stdin.readline().strip().split()

    if command[0] == "push":
        queue.push(int(command[1]))
    elif command[0] == "pop":
        queue.pop()
    elif command[0] == "size":
        queue.size()
    elif command[0] == "empty":
        queue.empty()
    elif command[0] == "front":
        queue.front()
    elif command[0] == "back":
        queue.back()
