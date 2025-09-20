import sys
input = sys.stdin.readline

import heapq as hq


def dijkstra(graph,start) :
    dis = [1e9] * (N+1)

    q = []
    hq.heappush(q,(0,start))
    dis[start] = 0


    while q :
        cw,cv = hq.heappop(q)

        if dis[cv] < cw :
            continue

        for nv,nw in graph[cv] :
            next = cw + nw
            if dis[nv] > next :
                dis[nv] = next
                hq.heappush(q,(next,nv))

    return dis

N,E = list(map(int,input().split()))
graph = [[] for _ in range(N+1)]


for _ in range(E) :
    a,b,c = list(map(int,input().split()))
    graph[a].append((b,c))
    graph[b].append((a,c))

# 거쳐야 할 정점
v1,v2 = list(map(int,input().split()))

s_dis = dijkstra(graph,1)
v1_dis = dijkstra(graph,v1)
v2_dis = dijkstra(graph,v2)

ver1 = s_dis[v1] + v1_dis[v2] + v2_dis[N]
ver2 = s_dis[v2] + v2_dis[v1] + v1_dis[N]

if ver1 >= 1e9 and ver2 >= 1e9 :
    ans = -1
else :
    ans = min(ver1,ver2)

print(ans)