from collections import deque

def solution(one, two):
    
    one_sum = sum(one)
    two_sum = sum(two)
    target = (one_sum + two_sum) // 2
    N = len(one)

    # 홀수면 못구함
    if (one_sum + two_sum) % 2 != 0 :
        return -1
    
    
    one = deque(one)
    two = deque(two)
    ans = 0
    
    while True :
        # 한 바퀴 돌아도 답이 안나오면 종료
        if ans >= 4*N :
            return -1
        
        if one_sum == two_sum :
            return ans
        
        if one_sum > two_sum :
            p = one.popleft()
            one_sum -= p
            two.append(p)
            two_sum += p
        
        else :
            p = two.popleft()
            two_sum -= p
            one.append(p)
            one_sum += p
            
        ans += 1
        
    return ans
        