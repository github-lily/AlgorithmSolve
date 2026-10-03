def solution(begin, target, words):
    N = len(words)
    word_len = len(begin)
    visit = [0] * N
    mn = int(1e9)
    
    def canChange(now, nxt) :
        diff = 0
        for i in range(word_len) :
            if now[i] != nxt[i] :
                diff += 1
                
            if diff > 1 :
                return False
        
        return True
    
    def dfs(cur, cnt, v) :
        nonlocal mn
        res = 0
        
        for idx in range(N) :
            if v[idx] == 0 and canChange(cur, words[idx]) :
                if words[idx] == target :
                    mn = min(cnt+1, mn)
                    continue

                
                v[idx] = 1
                res = dfs(words[idx], cnt + 1, v)
                v[idx] = 0

        return mn
    
    ans = dfs(begin, 0, visit)
    
    if mn == int(1e9) :
        return 0
    
    
    return ans      
        
    
    
    