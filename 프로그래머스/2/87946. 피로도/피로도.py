def solution(k, dungeons):
    mx = 0
    n = len(dungeons)
    v = [0] * n
    
    def dfs(stamina, cnt) :
        nonlocal mx
        
        if mx < cnt :
            mx = cnt
        
        if stamina <= 0 :
            return
        
        for i in range(n) :
            need, burn = dungeons[i]
            if stamina >= need and v[i] == 0 :
                v[i] = 1
                dfs(stamina - burn, cnt + 1)
                v[i] = 0
                
    dfs(k, 0)
    
    return mx
            
        
        