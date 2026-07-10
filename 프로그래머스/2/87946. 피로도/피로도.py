def solution(k, duns):
    n = len(duns)
    v = [False] * n
    mx = 0
    
    def dfs(health, cnt) :
        nonlocal mx
        
        mx = max(cnt,mx)
        
        if health <= 0 :
            return
        
        for i in range(n) :
            if v[i] == 0 and duns[i][0] <= health :
                v[i] = True
                dfs(health - duns[i][1], cnt + 1)
                v[i] = False
        
    
    dfs(k,0)
    
    return mx

        