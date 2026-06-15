import heapq

def solution(scovilles, K):
    cnt = 0
    q = []
    for scoville in scovilles :
        heapq.heappush(q,scoville)
    
    while q :        
        # 종료 조건 : q의 최소값이 K 이상 
        if q[0] >= K :
            return cnt
        
        if len(q) == 1 :
            if q[0] < K :
                return -1
        
        # 안되면 섞기
        x1 = heapq.heappop(q)
        x2 = heapq.heappop(q)
        
        new = x1 + (x2 * 2)
        cnt += 1
        
        heapq.heappush(q,new)
        
    return -1
            
            
        
        