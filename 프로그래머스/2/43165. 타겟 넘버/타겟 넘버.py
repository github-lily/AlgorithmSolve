def solution(numbers, target):
    ans = 0
    N = len(numbers)
    
    def dfs(num, i) :
        nonlocal ans, target, N
        if i == N :
            if num == target :
                ans += 1
            return
        
        dfs(num+numbers[i], i+1)
        dfs(num-numbers[i], i+1)
    
    dfs(0,0)
    
    return ans