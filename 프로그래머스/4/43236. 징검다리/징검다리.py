def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left = 0
    right = distance+1
    
    lenn = len(rocks)
    ans = 0
    
    while left < right :
        mid = (left + right) // 2
        
        remove = 0
        prev = 0
        
        for i in range(lenn) :
            cur = rocks[i]
        
            if cur - prev >= mid :
                # 간격이 현재 최소값보다 크면 통과
                prev = cur

            else :
                # 간격이 현재 최소값보다 작으면 최소값 후보 제거
                remove += 1
                if remove > n :
                    break

        # 제거해야 할 바위보다 많이 제거
        if remove > n :
            right = mid 

        else :
            left = mid+1
            if ans < mid :
                ans = mid
    
    return ans
        
            
            
        
        
    
    