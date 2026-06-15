def solution(want, number, discount):
    # 가지치기 1 : 원하는게 할인 안하면 종료
    if len(set(want) - set(discount)) > 0 :
        return 0
    
    ans = 0
    N = sum(number)
    D = len(discount)
    
    # 가지치기 2 : 할인일이 원하는 구매 개수보다 적으면 종료
    if N > D :
        return 0
    
    
    # want 저장
    needs = {}
    for i in range(len(number)) :
        needs[want[i]] = number[i]
    
    def check(dic) :
        vals = dic.values()
        for val in vals :
            if val > 0 :
                return False
        return True
    
    
    # 필요한 구매 물품 개수만큼 할인 품목 저장
    for idx in range(N) :
        prod = discount[idx]
        if prod in needs :
            needs[prod] -= 1
    
    # 확인
    if check(needs) :
        ans += 1

    # 범위 옮겨가며 확인
    for i in range(D-N) :

        # 맨 앞 물건 삭제
        de = discount[i]
        if de in needs :
            needs[de] += 1
        
        # 뒷 물건 추가
        ad = discount[i+N]
        if ad in needs :
            needs[ad] -= 1

        if check(needs) :
            ans += 1
            
    return ans
        
            
    

        
        
    
    
    # 최대 10개 구매
    