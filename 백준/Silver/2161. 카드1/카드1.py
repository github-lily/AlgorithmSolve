import sys
from collections import deque

def solve():
    try:
        line = sys.stdin.read().split()
        if not line:
            return
        n = int(line[0])
    except EOFError:
        return

    cards = deque(range(1, n + 1))
    discarded = []

    while len(cards) > 1:
        discarded.append(cards.popleft())
        cards.append(cards.popleft())

    discarded.append(cards[0])

    print(*(discarded))

if __name__ == "__main__":
    solve()