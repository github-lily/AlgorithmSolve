import sys
input = sys.stdin.readline

import heapq


def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    dp[0] = 0

    while q :
        w, cur = heapq.heappop(q)

        if dp[cur] < w :
            continue

        for next, nw in graph[cur] :
            cost = w + nw
            if dp[next] > cost :
                dp[next] = cost
                heapq.heappush(q,(cost,next))



N, D = map(int,input().split())
graph = [[] for _ in range(D+1)]
INF = 1e9
dp = [INF] * (D+1)

# 지름길 저장
for _ in range(N) :
    s,e,v = map(int,input().split())
    if e <= D :
        graph[s].append((e,v))

# 원래 경로 저장
for i in range(D) :
    graph[i].append((i+1,1))

dijkstra(0)
print(dp[D])
