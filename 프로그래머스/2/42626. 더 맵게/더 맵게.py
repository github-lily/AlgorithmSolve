import heapq as hq

def solution(scovilles, K):
    cnt = 0
    q = []
    
    for s in scovilles :
        hq.heappush(q,s)
    
    while q :            
        cur = hq.heappop(q)
        if cur >= K :
            return cnt
        
        if not q :
            return -1
        
        nxt = hq.heappop(q)
        hq.heappush(q,(cur + nxt*2))
        cnt += 1
    
    return -1
        
    
    
    