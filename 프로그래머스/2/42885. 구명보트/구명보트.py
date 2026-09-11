def solution(people, limit):
    people.sort(reverse = True)
    lenn = len(people)
    
    left = 0
    right= lenn-1
    cnt = 0
    
    while left <= right :
        # 마지막 사람
        if left == right :
            cnt += 1
            break
            
        # 2명 탑승
        if people[left] + people[right] <= limit :
            right -= 1
        
        # 왼쪽 한 명은 무조건 탑승
        left += 1
        cnt += 1
    
    return cnt
            
                    
                
    