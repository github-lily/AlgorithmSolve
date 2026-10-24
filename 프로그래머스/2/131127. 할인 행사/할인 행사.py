def solution(want, number, discount):
    inn = 0
    out = 0
    ans = 0
    
    D = len(discount)
    N = len(want)
    need = N
    summ = sum(number)

    
    # 필요 물품 저장
    wants = dict()
    
    for i in range(N) :
        wants[want[i]] = number[i]
    
    
    # 초반 N개 차감
    while inn < summ :
        cur = discount[inn]
        if cur in wants :
            wants[cur] -= 1
            if wants[cur] == 0 :        # 중복 need차감 방지
                need -= 1
        inn += 1
    
    if need < 1 :
        ans += 1
    

    # 가능한 날 탐색
    while inn < D :
        # 물건 제거
        out_prod = discount[out]
        if out_prod in wants :
            wants[out_prod] += 1
            if wants[out_prod] == 1 :
                need += 1
        
        
        # 물건 추가
        inn_prod = discount[inn]
        if inn_prod in wants :
            wants[inn_prod] -= 1
            if wants[inn_prod] == 0 :
                need -= 1
        
        out += 1
        inn += 1
        if need == 0 :
            ans += 1
        

    
    return ans
