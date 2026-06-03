def solution(citations):
    n = len(citations)
    cits = citations.sort(reverse=True)
    h = 0
    
    for i in range(n) :
        if i+1 <= citations[i] :
            h = i+1
        else :
            break
        
    return h