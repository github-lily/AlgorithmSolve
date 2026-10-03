def solution(begin, target, words):
    N = len(words)
    word_len = len(begin)
    v = [0] * N
    mn = int(1e9)
    
    def canChange(now, nxt) :
        diff = 0
        for i in range(word_len) :
            if now[i] != nxt[i] :
                diff += 1
                
            if diff > 1 :
                return False
        
        return diff == 1
    
    def dfs(cur, cnt) :
        nonlocal mn
        res = 0
        
        for idx in range(N) :
            if v[idx] == 0 and canChange(cur, words[idx]) :
                if words[idx] == target :
                    mn = min(cnt+1, mn)
                    continue

                
                v[idx] = 1
                dfs(words[idx], cnt + 1)
                v[idx] = 0

        return mn
    
    ans = dfs(begin, 0)
    
    return 0 if mn == int(1e9) else mn    
        
    
    
    