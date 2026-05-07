def solution(progresses, speeds):
    ans = []
    n = len(progresses)
    needs = []
    
    # 필요 일수 구하기
    for progress, speed in zip(progresses, speeds) :
        remain = 100 - progress
        need = (remain + speed - 1) // speed        # 올림 나눗셈
        needs.append(need)
        
    days = needs[0]
    cnt = 0
    
    # 묶기
    for need in needs :
        if days >= need :
            cnt += 1
        else :
            ans.append(cnt)
            days = need
            cnt = 1
            
    ans.append(cnt)     # 맨 뒤에거 넣어주기
    
    return ans