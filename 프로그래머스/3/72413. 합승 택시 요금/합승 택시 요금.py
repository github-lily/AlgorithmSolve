import heapq as hq

        
def dijkstra(start,graph,n) :
    dis = [int(1e9)] * (n+1)
    q = []    
    dis[start] = 0
    hq.heappush(q,(0,start))
    
    # 다익스트라
    while q :
        cw, cv = hq.heappop(q)
        if dis[cv] < cw : continue
        
        for nv,nw in graph[cv] :
            new_w = cw+nw
            if dis[nv] > new_w :
                dis[nv] = new_w
                hq.heappush(q,(new_w,nv))
                
    return dis
    

    
def solution(n, s, a, b, fares):
    
    graph = [[] for _ in range(n+1)]

    
    for i,j,f in fares :
        graph[i].append((j,f))
        graph[j].append((i,f))
    
    
    s_dis = dijkstra(s,graph,n)   
    a_dis = dijkstra(a,graph,n)
    b_dis = dijkstra(b,graph,n)

    
    mn = int(1e9)
    for k in range(1,n+1) :
        fare = s_dis[k] + a_dis[k] + b_dis[k]       # s -> k -> a/b  (s == k 일때가 각각 갈때 요금)
        if mn > fare :
            mn = fare
            
    return mn
    
    
    
    
        



        
        
    