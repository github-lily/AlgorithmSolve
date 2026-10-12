def solution(clothes):
    closet = dict()
    
    for cloth, typ in clothes :
        if typ not in closet :
            closet[typ] = 0
        closet[typ] += 1
        
    ans = 1
    for cnt in closet.values() :
        ans *= (cnt+1)
    
    return ans - 1
    