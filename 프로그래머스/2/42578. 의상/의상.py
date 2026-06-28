def solution(clothes):
    wardrobe = dict()
    ans = 1
    
    for cloth, typ in clothes :
        if typ not in wardrobe :
            wardrobe[typ] = []
        wardrobe[typ].append(cloth)
    
    
    for w in wardrobe.keys() :
        ans *= (len(wardrobe[w]) + 1)
    
    return ans -1       # 모두 안입은 경우 하나 제외