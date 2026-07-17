def solution(citations):
    cnt = 0
    citations.sort(reverse = True)
    
    for c in citations :
        cnt += 1
        if c >= cnt :
            continue
        
        # 현재 개수보다 인용 횟수가 적으면 중단
        else :
            return cnt-1
        
    return cnt