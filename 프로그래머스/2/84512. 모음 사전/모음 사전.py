   
def solution(target):
    alphabet = "AEIOU"
    cnt = 0
    
    def dfs(word) :
        nonlocal cnt
        
        if word == target :
            return True
        
        if len(word) == 5 :
            return False
        
        for a in alphabet :
            cnt += 1
            if dfs(word + a) :
                return True

        return False
            
    dfs("")
    
    return cnt
    
    
    
    
    
