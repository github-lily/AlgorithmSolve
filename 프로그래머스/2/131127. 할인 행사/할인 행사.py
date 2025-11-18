def check(dic) :  
    vals = dic.values()
    if all( 1 > val for val in vals) :
        return True
    return False
        
        
def solution(want, number, discount):
    N = sum(number)
    
    want_dict = dict()
    ans = 0
    
    # 딕셔너리에 저장
    for idx in range(len(number)) :
        want_dict[want[idx]] = number[idx]


    # 개수에 맞게 일단 차감
    for i in range(N) :
        if discount[i] in want :
            want_dict[discount[i]] -= 1
    
    # 구매가능한 날인지 확인
    if check(want_dict) :
        ans += 1
    
    idx = N
    
    # N일 이후 되는날 찾기
    while idx < len(discount) :
        if discount[idx-N] in want :
            want_dict[discount[idx-N]] += 1 
        if discount[idx] in want :
            want_dict[discount[idx]] -= 1
        
        if check(want_dict) :
            ans += 1
        idx += 1
        
    
    return ans
