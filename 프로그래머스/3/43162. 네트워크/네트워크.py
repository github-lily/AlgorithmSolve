from collections import deque

def solution(n, computers):
    cnt = 0
    graph = [[] for _ in range(n)]
    
    # 간선 정보 저장
    for i in range(n) :
        for j in range(n) :
            # 양방향 연결
            if i != j and computers[i][j] == 1 :
                graph[i].append(j)
    
    
    def bfs(start) :
        nonlocal visit
        q = deque([start])
        visit[start] = True
        
        while q :
            cur = q.popleft()
            
            for nxt in graph[cur] :
                if not visit[nxt] :
                    visit[nxt] = True
                    q.append(nxt)
        
        
    visit = [False] * n
    

    for i in range(n) :
        if not visit[i] :
            cnt += 1
            bfs(i)
    
    return cnt
    
    
    