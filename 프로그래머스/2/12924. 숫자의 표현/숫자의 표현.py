def solution(n):
    ans = 0
    
    # 누적합 리스트 만들기
    prefix = [0] * (n+1)
    for i in range(1,n+1) :
        prefix[i] = prefix[i-1] + i
    
    # 투포인터로 탐색
    head = 1
    tail = 0
    
    while head <= n and head != tail:
        sm = prefix[head] - prefix[tail]
        if sm == n :
            head += 1
            ans += 1
        elif sm > n :
            tail += 1
            if tail >= head :
                head += 1
        else :  # sm < n
            head += 1
        
    
            
    return ans
    
    