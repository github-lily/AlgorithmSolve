def solution(clothes):
    
    wardrobe = {}
    
    for name, typ in clothes :
        if typ not in wardrobe :
            wardrobe[typ] = []
        wardrobe[typ].append(name)

    tmp = 1
    
    for w in wardrobe :
        tmp *= len(wardrobe[w])+1
        
    return tmp - 1      # 아무것도 안입은 경우 제외
    