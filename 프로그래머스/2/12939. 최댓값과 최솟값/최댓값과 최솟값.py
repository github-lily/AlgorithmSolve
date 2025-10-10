def solution(s):
    nums = []
    for num in s.split() :
        nums.append(int(num))
    
    return f'{min(nums)} {max(nums)}'