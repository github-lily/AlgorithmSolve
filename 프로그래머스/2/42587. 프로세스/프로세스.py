def solution(priorities, location):
    orders = sorted(priorities, reverse = True)
    now_top = 0
    cnt = 0
    
    while True :
        for idx, val in enumerate(priorities) :
            if val == orders[now_top] :
                cnt += 1
                now_top += 1
                if idx == location :
                    return cnt
                
        
    
    
    
    

        
        
    