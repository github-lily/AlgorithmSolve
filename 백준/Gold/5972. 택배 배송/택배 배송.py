import heapq

def dijkstra(start) :

    # 초기 준비
    q = []
    v = [INF] * (N+1)

    heapq.heappush(q,(0,start))
    v[start] = 0


    while q :
        weight, now = heapq.heappop(q)

        if v[now] < weight :
            continue

        for nx_weight, next in graph[now] :
            cost = v[now] + nx_weight
            if v[next] > cost :
                v[next] = cost
                heapq.heappush(q,(nx_weight,next))

    return v[N]


# N : 노드의 수(1~N) , M : 간선의 수
N,M = map(int,input().split())
INF = float(1e9)

# 간선 정보 저장
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    s,e,w = map(int,input().split())
    graph[s].append((w,e))      # 가중치, 도착지점
    graph[e].append((w,s))      # 양방향 그래프

ans = dijkstra(1)

print(ans)
