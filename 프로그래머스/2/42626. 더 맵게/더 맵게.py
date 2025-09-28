import heapq as hq

def solution(scoville, K):
    q = []
    
    for score in scoville :
        hq.heappush(q,score)
        
    cnt = 0
    
    while q[0] < K :
        if len(q) < 2 :
            return -1
        
        f1 = hq.heappop(q)
        f2 = hq.heappop(q)
        
        spicy = f1 + (f2*2)
        cnt += 1
        
        hq.heappush(q,spicy)
        
    return cnt