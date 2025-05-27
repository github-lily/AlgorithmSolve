import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    score = float(input())
    if len(heap) < 7:
        heapq.heappush(heap, -score)  # 최대 힙 구현 위해 음수로 저장
    else:
        if -heap[0] > score:  # 현재 가장 큰 값보다 작으면 교체
            heapq.heappop(heap)
            heapq.heappush(heap, -score)

result = sorted([-x for x in heap])
for num in result:
    print(f"{num:.3f}")
