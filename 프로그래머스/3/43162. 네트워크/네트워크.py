def solution(n, computers):
    v = [0] * n
    cnt = 0
    
    def dfs(idx) :
        nonlocal v
        
        v[idx] = 1
                
        for j in range(n) :
            if v[j] == 0 and computers[idx][j] == 1 :       # 방문안한 인접 정점
                dfs(j)

    
    
    for i in range(n) :
        if v[i] == 0 :
            dfs(i)
            cnt += 1
            
    
    
    return cnt