def solution(citations):
    h = 0
    cnt = 0
    citations.sort(reverse = True)
    
    for c in citations :
        cnt += 1
        if c >= cnt :
            continue
        else :
            return cnt-1
        
    return cnt