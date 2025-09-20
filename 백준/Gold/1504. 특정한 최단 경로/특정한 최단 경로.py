
import heapq


INF = int(1e9)
N,E = map(int,input().split())
connect = [[] for _ in range(N+1)]      # 정점번호 1부터 시작


for _ in range(E) :
    a,b,c = map(int,input().split())
    connect[a].append((b,c))
    connect[b].append((a,c))
    

# 방문해야하는 포인트
p1,p2 = map(int,input().split())


# 시작점부터 각 노드까지의 최단경로 함수
def dikjstra(start) :
    distance = [INF]*(N+1)                      # 시작점부터 각 노드까지의 최단경로 리스트

    q = []
    heapq.heappush(q,(0,start))           # 시작지점은 거리 0
    distance[start] = 0

    while q :
        now_distance, node = heapq.heappop(q)


        if distance[node] < now_distance :
            continue

        for next, next_distance in connect[node] :
            total_distance = next_distance + now_distance
            if distance[next] > total_distance :
                distance[next] = total_distance
                heapq.heappush(q,(total_distance,next))

    return distance


from_start = dikjstra(1)
from_p1 = dikjstra(p1)
from_p2 = dikjstra(p2)

# 최단 경로는 1 -> p1 -> p2 -> N 또는 1-> p2 -> p1 -> N 둘 중 하나
route1 = from_start[p1] + from_p1[p2] + from_p2[N]
route2 = from_start[p2] + from_p2[p1] + from_p1[N]


ans = min(route1, route2)

if ans >= INF :
    ans = -1
    
print(ans)
