def solution(k, gyuls):
    
    # 귤 개수 저장
    cnt_dict = {}
    
    for g in gyuls :
        if g not in cnt_dict :
            cnt_dict[g] = 0
        cnt_dict[g] += 1
    
    # 귤 고르기
    vals = list(cnt_dict.values())      # 개수만 필요
    vals.sort(reverse = True)
    ans = 0
    
    for v in vals :
        k -= v
        ans += 1
        if k <= 0 :
            return ans
    
    return ans
        
    
    