from collections import Counter

def solution(topping):
    answer = 0
    right_count = Counter(topping)
    left_set = set()
    
    for t in topping:
        left_set.add(t)
        right_count[t] -= 1
        
        if right_count[t] == 0:
            del right_count[t]
            
        if len(left_set) == len(right_count):
            answer += 1
            
    return answer