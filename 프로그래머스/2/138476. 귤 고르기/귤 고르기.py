from collections import Counter
def solution(k, tangerine):
    cnt = sorted(Counter(tangerine).values(), reverse = True)
    
    ans = 0
    summ = 0
    for x in cnt :
        summ += x
        ans += 1
        if summ >= k :
            break
            
    return ans