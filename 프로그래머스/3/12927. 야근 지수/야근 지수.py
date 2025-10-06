import heapq as hq

def solution(n, works):
    # 야근 피로도 = 야근 시작 시점에서 남은 일의 작업량을 제곱하여 더한 값
    
    total = sum(works)
    if total <= n :
        return 0
    
    
    q = []
    
    for i in range(len(works)) :
        hq.heappush(q,-works[i])        # 최대힙 활용
        
    while n > 0 :
        val = hq.heappop(q) 
        n -= 1
        hq.heappush(q,val+1) # val이 음수니까 1을 더해주기
    
    ans = sum(x**2 for x in q)
    return ans
        
    

    
    