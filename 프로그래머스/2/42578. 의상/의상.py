from collections import defaultdict

def solution(clothes):
    closet = defaultdict(int)
    
    for cloth in clothes :
        closet[cloth[1]] += 1
    
    print(closet)
    
    if len(closet) == 1 :
        key,val = closet.popitem()
        return val
    
    ans = 1
    for i in closet.values() :
        ans *= i+1      # 입는경우(옷의종류개수) + 안입는경우(1)
    
    return ans-1
        
        