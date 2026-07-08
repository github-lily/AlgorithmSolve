def solution(numbers):
    # 문자열로 바꿔서 순서 배치, 0 고려하기
    nums = [x*3 for x in map(str,numbers)]
    nums.sort(reverse = True)
    
    ans = ""
    for num in nums :
        l = len(num) // 3
        ans += num[:l]
    
    if ans[0] == "0" :
        ans = "0"
    return ans
