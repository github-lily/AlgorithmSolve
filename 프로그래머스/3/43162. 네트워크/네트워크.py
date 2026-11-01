from collections import deque

def solution(n, computers):
    ans = 0
    graph = [[] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if i == j :
                continue
            if computers[i][j] == 1 :
                graph[i].append(j)
    
    q = deque()
    v = [0] * n
    
    for i in range(n) :
        if v[i] == 0 :
            q.append(i)
            v[i] = 1
            ans += 1
            
            while q :
                cur = q.popleft()
                
                for nxt in graph[cur] :
                    if v[nxt] == 0 :
                        v[nxt] = 1
                        q.append(nxt)
        
    return ans
        
                        
    