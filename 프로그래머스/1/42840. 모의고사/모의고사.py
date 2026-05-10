def solution(answers):    
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]              # 8개
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]      # 10개
    
    cnt = [0,0,0]
    

    for i in range(len(answers)) :
        ans = answers[i]
        if ans == one[i%5] :
            cnt[0] += 1
        if ans == two[i%8] :
            cnt[1] += 1
        if ans == three[i%10] :
            cnt[2] += 1
            
    # 값이 같을 경우
    if cnt[0] == cnt[1] and cnt[1] == cnt[2] :
        return [1,2,3]
    
        
    mx_idx = 0
    mx_val = max(cnt)
    result = []

    for idx,val in enumerate(cnt) :
        if val == mx_val :
            result.append(idx+1)
            
    return result
    
    
        
        
    