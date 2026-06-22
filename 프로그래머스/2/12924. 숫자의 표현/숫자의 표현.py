def solution(n):
    ans = 0

    # 투포인터로 탐색
    left = 0
    right = 0
    summ = 0
    
    while right <= n :
        if summ == n :
            ans += 1
            right += 1
            summ += right

        elif summ < n :
            right += 1
            summ += right
        
        else : #summ > n
            left += 1
            summ -= left
    
    return ans

    