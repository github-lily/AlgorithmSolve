import math

def solution(progresses, speeds):
    ans = []
    days = 0
    cnt = 0
    N = len(progresses)
    idx = 0
    
    while idx < N :
        needs = math.ceil((100 - progresses[idx]) / speeds[idx])
        
        if days == 0 :
            days = needs
            cnt += 1
        else :
            # 함께 배포
            if needs <= days :
                cnt += 1
            # 따로 배포
            else :
                ans.append(cnt)
                cnt = 1
                days = needs
        
        idx += 1
    
    if cnt :
        ans.append(cnt)
        
    return ans
        
        
    
    