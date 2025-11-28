def solution(phone_book):
    ans = True
    
    def check(cur,nxt) :
        for k in range(min(len(cur),len(nxt))) : 
            if cur[k] != nxt[k] :
                return False
        return True
    
    N = len(phone_book)
    phone_book.sort()

    
    for i in range(N-1) :
        cur = phone_book[i]
        nxt = phone_book[i+1]
            
        if check(cur,nxt) :
            ans = False
            return ans
        
    return ans
            

            
            
        
            