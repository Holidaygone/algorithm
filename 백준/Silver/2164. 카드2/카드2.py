from collections import deque

N = int(input())

card = deque(range(1, N + 1))

while len(card) > 1:
    card.popleft()
    first_Card = card.popleft()
    card.append(first_Card)

print(card[0])