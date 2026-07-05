def solution(participant, completion):
    parti = dict()
    
    for p in participant :
        if p not in parti :
            parti[p] = 1
        else :
            parti[p] += 1
    
    for c in completion :
        parti[c] -= 1
    
    for p in parti :
        if parti[p] :
            return p

    
    
    