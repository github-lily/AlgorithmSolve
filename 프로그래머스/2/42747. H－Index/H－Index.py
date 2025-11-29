def solution(cit):
    
    cit.sort(reverse = True)
    h = 0
    
    for i in range(len(cit)) :
        if cit[i] >= i+1 :
            h = i + 1
        else :
            break
            
    return h
        