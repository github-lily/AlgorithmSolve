def solution(clothes):
    # 종류별 옷 개수 카운트
    cnt = dict()
    for cloth,typ in clothes :
        if typ not in cnt :
            cnt[typ] = 1
        else :
            cnt[typ] += 1
    
    # A 3개 B 2개 C 4개 있을 때 경우의 수
    # 각각 N+1개(아무것도 안고른 경우) - ABC 중 아무것도 안 고른 경우의 수 1 
    # (4 * 3 * 5) - 1  = 59개
    
    vals = cnt.values()
    ans = 1
    
    for val in vals :
        ans *= (val+1)
        
    return ans - 1      
