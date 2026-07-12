from collections import deque

def solution(n, computers):
    v = [0] * n
    graph = [[] for _ in range(n)]
    ans = 0
    
    for i in range(n) :
        for j in range(n) :
            if i == j :
                continue
            if computers[i][j] == 1 :
                graph[i].append(j)
                
                
    def bfs(start) :
        q = deque([start])

        while q :
            cur = q.popleft()
            for nxt in graph[cur] :
                if v[nxt] == 0 :
                    q.append(nxt)
                    v[nxt] = 1
                    
    
    for idx in range(n) :
        if v[idx] == 1 :
            continue
        bfs(idx)
        ans += 1
    
    return ans
        