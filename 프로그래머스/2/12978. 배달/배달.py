import heapq as hq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    dis = [float('inf')] * (N+1)
    
    for s,e,w in road :
        graph[s].append((e,w))
        graph[e].append((s,w))
    
    q = []
    dis[1] = 0
    hq.heappush(q,(0,1))
    
    while q :
        cw, cv = hq.heappop(q)
        
        if dis[cv] < cw :
            continue
        
        for nv, nw in graph[cv] :
            if dis[nv] > cw + nw :
                dis[nv] = cw + nw
                hq.heappush(q,(dis[nv],nv))
                
    print(dis)
        
    ans = 0
    for i in range(1,N+1) :
        if dis[i] <= K :
            ans += 1
    
    return ans
        
        
    