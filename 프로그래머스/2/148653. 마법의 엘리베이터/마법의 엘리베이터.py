def solution(storey):
    cnt = 0
    
    while storey > 0 :
        remain = storey % 10
        
        if remain > 5 :
            cnt += (10 - remain)
            storey += (10 - remain)
            
        elif remain < 5 :
            cnt += remain       
            
        else  :
            nxtRemain = (storey // 10) % 10
            # 반올림
            if nxtRemain >= 5 :
                storey += 5            
            # 반내림
            else :
                storey -= 5
                
            cnt += 5
                
        storey = storey // 10
    
    
    return cnt
        
    
    