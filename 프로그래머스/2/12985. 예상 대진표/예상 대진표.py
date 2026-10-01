def solution(n,a,b):
    if a > b :
        a,b = b,a
        
    left = 0
    right = n
    cnt = n.bit_length() - 1
    
    while left < right :
        mid = (left + right) // 2
        
        # 중앙 기준으로 양끝에 있으면 구간의 끝(결승)에서 만남
        if a <= mid < b :
            return cnt
        
        # a,b 둘 다 왼쪽
        if b <= mid :
            right = mid
        
        else :
            left = mid + 1
        
        cnt -= 1
        
    
    