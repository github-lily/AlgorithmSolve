def solution(prices):
    lenn = len(prices)
    ans = [0] * lenn
    
    stack = []
    
    for i in range(lenn-1,-1,-1) :
        cur = prices[i]
        
        while stack and prices[stack[-1]] >= cur :
            stack.pop()
            
        if not stack :
            ans[i] = lenn-1-i
            
        else :
            ans[i] = stack[-1] -i
            
        stack.append(i)
        
    return ans
    