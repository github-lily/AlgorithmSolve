def solution(numbers, target):
    lenn = len(numbers)
    ans = 0
    
    def dfs(i, summ) :
        nonlocal ans
        if i == lenn :
            if summ == target :
                ans += 1
            return
        
        dfs(i+1, summ + numbers[i])
        dfs(i+1, summ - numbers[i])
    
    dfs(0,0)
    
    return ans