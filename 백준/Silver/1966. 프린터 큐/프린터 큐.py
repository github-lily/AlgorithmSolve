from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    indexed_queue = deque([(i, p) for i, p in enumerate(queue)])
    count = 0

    while indexed_queue:
        current = indexed_queue.popleft()
        if any(current[1] < item[1] for item in indexed_queue):
            indexed_queue.append(current)
        else:
            count += 1
            if current[0] == M:
                print(count)
                break
