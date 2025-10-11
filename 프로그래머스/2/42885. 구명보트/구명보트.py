def solution(lst, limit):
    
    lst.sort(reverse = True)
    
    N = len(lst)
    ans = 0
    
    # 한 보트당 최대 2명 태울 수 있으니 투포인터 + 그리디 접근
    i = 0
    j = N-1
    
    
    while i <= j :
            
        if lst[i] == limit :
            ans += 1
            i += 1
        else :
            if i != j and  lst[i] + lst[j] <= limit :
                j -= 1
            i += 1
            ans += 1
            
        
        
    return ans
            
            
            
    
            