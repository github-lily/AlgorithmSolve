def solution(participants, completion):
    participant = dict()
    
    for p in participants :
        if p not in participant :
            participant[p] = 1
        else :
            participant[p] += 1
    
    for c in completion :
        participant[c] -= 1
    
    for p in participant :
        if participant[p] :
            return p

    
    
    