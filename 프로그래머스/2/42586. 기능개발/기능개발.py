import math

def solution(progresses, speeds):
    
    ans = []
    n = len(progresses)
    idx = 0
    today = 0
    cnt = 0
    
    while idx < n :
        need_days = math.ceil((100 - progresses[idx])/speeds[idx])
        # 개발 완료
        if today >= need_days :
            cnt += 1
            idx += 1
        
        # 개발 미완료(날짜 부족)
        else :
            if cnt > 0 :
                ans.append(cnt)
                cnt = 0
            
            today = need_days
            idx += 1
            cnt += 1
    
    if cnt > 0 :
        ans.append(cnt)
        
    return ans
        
            
        
    
    