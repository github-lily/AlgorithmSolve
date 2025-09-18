from collections import deque



def solution(n, computers):
    answer = 0
    graph = [[]  for _ in range(n)]
    v = [0] * n
    

    # 그래프 저장
    for i in range(n) :
        for j in range(i+1,n) :     # i == j 거르기
            if computers[i][j] == 1 :
                graph[i].append(j)
                graph[j].append(i)      # 양방향      
    
    # 함수 구현부
    def bfs(start) :
        nonlocal v, graph

        q = deque([start])
        v[start] = 1

        while q :
            cur = q.popleft()
            for next in graph[cur] :
                if v[next] == 0 :
                    v[next] = 1
                    q.append(next)
    
    # 함수 호출부                    
    for node in range(n) :
        if v[node] == 0 :
            bfs(node)
            answer += 1
            

        
    
    
    
    return answer