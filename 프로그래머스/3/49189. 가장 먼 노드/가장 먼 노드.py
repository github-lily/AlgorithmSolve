# 1번 노드로부터 가장 멀리 떨어진 노드의 개수
# 양방향
from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range(n+1)]    # 1-index
    
    for a,b in vertex :
        graph[a].append(b)
        graph[b].append(a)
    
    visit = [-1] * (n+1)        # 거리 기록 방문배열
    start = 1
    
    
    q = deque([start])
    visit[start] = 0
    while q :
        cur = q.popleft()
        
        for nxt in graph[cur] :
            if visit[nxt] == -1  :
                visit[nxt] = visit[cur] + 1
                q.append(nxt)
                
    
    mx = max(visit)
    ans = visit.count(mx)
    return ans
    
    
    