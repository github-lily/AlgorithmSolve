def solution(progresses, speeds):
    ans = []
    N = len(progresses)
    
    # 필요 일수 구하기
    needs = []      # stack
    for i in range(N-1, -1, -1) :       # 뒤에서부터 넣기
        need = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0 :
            need += 1
        needs.append(need)
    
    # 개발 완료된 것끼리 묶기
    top = N-1
    days = needs[top]
    cnt = 1
    top -= 1
    
    while top > -1 :
        if needs[top] <= days :
            cnt += 1
            top -= 1
        else :
            if cnt != 0 :           # 값 저장
                ans.append(cnt)
                cnt = 0
            days += 1
    
    ans.append(cnt)
    
    return ans
        