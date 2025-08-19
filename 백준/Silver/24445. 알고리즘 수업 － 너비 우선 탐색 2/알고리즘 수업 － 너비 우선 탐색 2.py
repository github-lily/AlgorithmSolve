import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# 내림차순으로 탐색해야 함
for v in range(1, N + 1):
    g[v].sort(reverse=True)

order = [0] * (N + 1)
q = deque([R])
cnt = 1
order[R] = cnt

while q:
    cur = q.popleft()
    for nxt in g[cur]:
        if order[nxt] == 0:
            cnt += 1
            order[nxt] = cnt
            q.append(nxt)

print("\n".join(map(str, order[1:])))
