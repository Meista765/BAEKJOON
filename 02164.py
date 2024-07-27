from collections import deque

deck = deque(i for i in range(1, int(input())+1))

while len(deck) > 1:
    deck.popleft()
    deck.rotate(-1)

print(deck.pop())