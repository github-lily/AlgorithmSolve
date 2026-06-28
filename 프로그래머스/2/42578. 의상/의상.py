def solution(clothes):
    wardrobe = dict()
    ans = 1
    
    for cloth, typ in clothes :
        if typ not in wardrobe :
            wardrobe[typ] = 1
        wardrobe[typ] += 1
    
    
    for w in wardrobe.values() :
        ans *= w
    
    return ans -1       # 모두 안입은 경우 하나 제외