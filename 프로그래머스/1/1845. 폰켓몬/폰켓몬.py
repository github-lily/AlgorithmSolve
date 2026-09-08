def solution(nums):
    can_get = len(nums) // 2        # 항상 짝수
    nums_set_lenn = len(set(nums))
    
    return min(can_get, nums_set_lenn)
    