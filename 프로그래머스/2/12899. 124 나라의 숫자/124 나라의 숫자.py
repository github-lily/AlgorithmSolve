def solution(n):
    nums = ["1","2","4"]
    ans = []
    
    while n > 0 :
        n -= 1
        
        ans.append(nums[n % 3])
        
        n //= 3
    
    res = "".join(reversed(ans))
    return res
        
    
