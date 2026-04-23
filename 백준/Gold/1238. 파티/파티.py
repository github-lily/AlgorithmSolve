import heapq,sys
input = sys.stdin.readline


def dikstra(start,graph) :
    v = [int(1e9)] * (n+1)
    q = [(0,start)]
    v[start] = 0

    while q :
        cur_weight, cur = heapq.heappop(q)

        if v[cur] < cur_weight :
            continue

        for nxt_weight, nxt in graph[cur] :
            if v[nxt] > v[cur] + nxt_weight :
                v[nxt] = v[cur] + nxt_weight
                heapq.heappush(q,(v[nxt],nxt))

    return v


n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]

for _ in range(m) :
    s,e,t = map(int,input().split())
    graph[s].append((t,e))
    reverse_graph[e].append((t,s))


# x -> 모든지점
toAll = dikstra(x,graph)

# 모든지점 -> x (역순으로 돌아오며 체크)
toX = dikstra(x,reverse_graph)

max = 0
for i in range(1,n+1) :
    val = toAll[i] + toX[i]
    if max < val :
        max = val

print(max)
