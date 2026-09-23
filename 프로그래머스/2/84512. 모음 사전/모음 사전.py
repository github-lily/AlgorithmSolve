   
def solution(target):
    alphabet = "AEIOU"
    cnt = 0
    isTarget = False
    
    def dfs(word) :
        nonlocal cnt, isTarget
        if isTarget :
            return
            
    
        if word == target :
            isTarget = True
            return 
        
        if len(word) == 5 :
            return
        
        for i in range(5) :
            cnt += 1
            dfs(word + alphabet[i])
            if isTarget :
                return
            
    dfs("")
    
    return cnt
    
    
    
    
    
