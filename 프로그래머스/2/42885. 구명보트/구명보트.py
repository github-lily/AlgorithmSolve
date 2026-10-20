def solution(people, limit):
    people.sort(reverse = True)
    
    cnt = 0
    N = len(people)
    heavy = 0
    light = N-1
    
    while heavy <= light :
        if people[heavy] + people[light] <= limit :
            light -= 1
        
        heavy += 1
        cnt += 1
    
    return cnt