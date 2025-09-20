def solution(n, times):
    
    lo = 0
    hi = n * max(times)

    
    mn = int(1e9)
    
    while lo <= hi :
        mid = (lo+hi)//2
        can = check(mid,times)
        
        if can >= n :
            mn = mid
            hi = mid-1
        
        if can < n :
            lo = mid+1
            
    return mn
            
        
        
        
        
def check(target,times) :
    can = 0
    for time in times :
        can += target//time
    return can

        
         
    
        
        
    