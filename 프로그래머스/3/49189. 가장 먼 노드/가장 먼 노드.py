from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    v = [0] * (n+1)

    
    for a,b in edge :
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque([1]) 
    v[1] = 1

        
    while q :
        c = q.popleft()
        
        for next in graph[c] :
            if v[next] == 0 or v[next] > v[c] +1 :
                v[next] = v[c]+1
                q.append(next)
                
                
    ans = 0
    mx = max(v)
    
    for idx in range(1,n+1) :
        if v[idx] == mx :
            ans += 1
    
    return ans
            
    
    