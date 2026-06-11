def solution(part, comp):
    part.sort()
    comp.sort()
    
    for i in range(len(comp)) :
        if part[i] != comp[i] :
            return part[i]
    return part[-1]
        