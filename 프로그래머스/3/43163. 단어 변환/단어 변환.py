from collections import deque

def solution(begin, target, words):
    word_len = len(begin)
    lenn = len(words)
    
    q = deque([(0, begin)])
    v = [0] * lenn 
    

    def canChange(now, nxt) :
        diff = 0
        
        for i in range(word_len) :
            if now[i] != nxt[i] :
                diff += 1
        
            if diff > 1 :
                return False
        
        return diff == 1
    
    while q :
        cnt, cur = q.popleft()
        
        if cur == target :
            return cnt
        
        for i in range(lenn) :
            if v[i] == 0 and canChange(cur, words[i]) :
                v[i] = 1
                q.append((cnt+1, words[i]))
        
    
    return 0
        
        
    
