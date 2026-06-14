def solution(numbers, target):
    cnt = 0
    n = len(numbers)
    
    def dfs(num, i) :
        nonlocal cnt, target
        # 종료 조건
        if i == n :
            if num == target :
                cnt += 1
            return
        
        dfs(num+numbers[i], i+1)
        dfs(num-numbers[i], i+1)
    
    dfs(0, 0)
    
    return cnt