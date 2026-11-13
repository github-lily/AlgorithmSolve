def solution(n):
    
    def dfs(num) :
        if num == 0 :
            return 0
        
        if num % 2 == 0 :
            return dfs(num//2)
        
        return dfs(num-1) + 1 
        
    return dfs(n)