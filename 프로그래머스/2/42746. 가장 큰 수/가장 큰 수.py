def solution(numbers):
    nums = list(map(str,numbers))
    nums.sort(key = lambda x : x*3 , reverse = True)
    
    ans = "".join(nums)
    
    if ans[0] == "0" :
        ans = "0"
    
    return ans