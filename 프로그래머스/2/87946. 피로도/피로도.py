def solution(k, dun):
    n = len(dun)
    v = [False] * n
    mx = 0
    
    def dfs(energy,cnt) :
        nonlocal mx
        
        if mx < cnt :
            mx = cnt
        
        for i in range(n) :
            if v[i] :
                continue
            need, cost = dun[i][0], dun[i][1]
            if energy >= need :
                v[i] = True
                dfs(energy - cost, cnt + 1)
                v[i] = False
    
    dfs(k,0)
    return mx