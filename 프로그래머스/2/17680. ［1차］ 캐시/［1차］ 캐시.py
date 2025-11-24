from collections import deque

def solution(size, cities):
    
    if size == 0 :
        ans = len(cities) * 5
        return ans
    
    q = deque ()
    ans = 0
    
    for city in cities :
        city = city.lower()
        
        # cache hit  : 기존에 있는 값이면 제거
        if city in q :
            q.remove(city)  
            ans += 1
        
        # cache miss : 기존에 없던 값이면 가장 오래된 값(LRU) 제거 
        else :
            if len(q) == size :
                q.popleft()
            ans += 5
        q.append(city)
        
    return ans
        
        
    
    
    