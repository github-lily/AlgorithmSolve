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
        else :
            # 따로 배포
            if needs > days :
                ans.append(cnt)
                cnt = 0
                days = needs
        
        cnt += 1
        idx += 1
    
    if cnt :
        ans.append(cnt)
        
    return ans
        
        
    
    