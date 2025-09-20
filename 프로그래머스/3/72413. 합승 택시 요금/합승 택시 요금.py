
    
def solution(n, s, a, b, fares):
    
    graph = [[int(1e9)] *n for _ in range(n)]


    
    for i,j,f in fares :
        graph[i-1][j-1] = f
        graph[j-1][i-1] = f
    
    # 값 초기화
    for i in range(n) :
        graph[i][i] = 0
    
    for k in range(n) :
        for r in range(n) :
            for c in range(n) :
                if graph[r][c] > graph[r][k] + graph[k][c] :
                    graph[r][c] = graph[r][k] + graph[k][c]
    
    mn = int(1e9)          
    for i in range(n) :
        mn = min(mn, graph[s-1][i] + graph[i][a-1] + graph[i][b-1])
    
    return mn
                
    
    
    
    
        



        
        
    