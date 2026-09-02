from collections import deque

def solution(n, edge):
    # 양방향
    graph = [[] for _ in range(n+1)]
    
    for e1,e2 in edge :
        graph[e1].append(e2)
        graph[e2].append(e1)
        
    
    # 초기값 설정
    q = deque()
    start = 1
    v = [0] * (n+1)
    
    # 시작점 표시
    v[start] = 1
    q.append(start)
    
    # 탐색
    while q :
        cur = q.popleft()
        
        for nxt in graph[cur] :
            if v[nxt] == 0 or (v[nxt] > (v[cur] + 1)) :
                v[nxt] = v[cur] + 1 
                q.append(nxt)
    
    # 최대 길이 노드 개수 카운트
    ans = v.count(max(v))
    
    return ans