from collections import deque

def solution(x, y, n):
    q = deque([(x,0)])
    v = [0] * 1000001
    v[x] = 1
    
    while q :
        cur, cnt = q.popleft()
        
        if cur == y :
            return cnt
        
        if cur > y :
            continue
        
        for nxt in ((cur+n, cur*2, cur*3)) :
            if nxt <= y and v[nxt] == 0 :
                v[nxt] = 1
                q.append((nxt,cnt+1))
        
    
    return -1