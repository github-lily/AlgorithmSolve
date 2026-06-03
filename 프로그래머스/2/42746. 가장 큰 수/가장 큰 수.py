def solution(numbers):
    nums = list(map(str,numbers))
    
    # 파이썬 문자열 비교의 특징! 한글자씩 비교하기 때문에 333 > 303030
    nums.sort(key = lambda x : x*3, reverse = True)
    
    # [0,0,0] 이면 000이 나오니까 0이 나오도록 str -> int or 확인
    ans = ''.join(nums)
    
    if ans[0] == '0' :
        ans = '0'
    return ans
    
    