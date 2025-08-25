import sys
input = sys.stdin.readline

from collections import deque

def is_bipartite(V, adj):
    v = [0] * (V + 1)  # 0: 미방문, 1 / -1: 두 색

    for s in range(1, V + 1):
        if v[s] != 0:
            continue
        # s가 고립 정점이든 아니든, 새로운 컴포넌트 시작
        v[s] = 1
        q = deque([s])

        while q:
            cur = q.popleft()
            for nxt in adj[cur]:
                if v[nxt] == 0:
                    v[nxt] = -v[cur]   # 한 줄로 색 반전
                    q.append(nxt)
                elif v[nxt] == v[cur]:
                    return False               # 같은 색 이웃 → 이분그래프 아님
    return True

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    print("YES" if is_bipartite(V, adj) else "NO")
