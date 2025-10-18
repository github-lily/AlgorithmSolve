import heapq as hq

def solution(n, costs): 
    graph = [[] for _ in range(n)]

    # 가중치와 그래프정보 저장
    for n1,n2,w in costs :
        graph[n1].append((w,n2))
        graph[n2].append((w,n1))
    
    
    v = [0]*(n)
    q = [(0,0)]
    total = 0
    cnt = 0

    while q and cnt < n :       # cnt : 모든 정점 다 돌면 끝
        cw,ce = hq.heappop(q)
        
        if v[ce] == 1 :     # 방문한 곳이면 패스
            continue        
        
        v[ce] = 1
        total += cw
        cnt += 1
        for nw,ne in graph[ce] :
            if v[ne] == 0 :         # 방문 안한 정점이면 추가
                hq.heappush(q,(nw,ne))  
        
    return total
    
    
    
    