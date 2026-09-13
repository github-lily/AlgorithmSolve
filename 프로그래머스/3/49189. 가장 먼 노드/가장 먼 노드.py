from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    v = [0] * (n+1)
    
    q = deque([1])
    v[1] = 1
    
    for v1,v2 in edge :
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    
    while q :
        cur = q.popleft()
        
        for nxt in graph[cur] :
            if v[nxt] == 0 :
                v[nxt] = v[cur] + 1
                q.append(nxt)
        
    ans = v.count(max(v))
    return ans
    
    