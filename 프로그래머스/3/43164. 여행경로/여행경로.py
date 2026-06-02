def solution(tickets):
    tickets.sort()
    N = len(tickets)
    visit = [False] * N
    route = ['ICN']
    
    # 출발지 기준으로 도착지 저장
    graph = {}

    for start, end in tickets :
        if not start in graph :
            graph[start] = []
        graph[start].append(end)

    def dfs(cur) :
        # 종료 조건(모든 티켓 사용)
        if len(route) == N+1 :
            return True
        
        for i in range(N) :
            start, end = tickets[i]
            
            # 출발점이 같고 아직 방문 전이라면
            if start == cur and not visit[i] :
                visit[i] = True         # 티켓사용
                route.append(end)       # 방문
                
                if dfs(end) :
                    return True    # 종료
                
                # end를 넣었는데, False가 나오면 빠꾸(끝까지 갔는데 종료조건 미충족 경우)
                route.pop()
                visit[i] = False
                
        return False
                
              
    dfs('ICN')
    
    return route
                
  