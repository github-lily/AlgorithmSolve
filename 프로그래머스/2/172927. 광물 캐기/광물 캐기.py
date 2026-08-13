def solution(picks, minerals):
    # 캘 수 있는 광석 개수만큼만 계산
    minerals = minerals[:sum(picks)*5]
    N = len(minerals)
    
    groups = []
    
    # 5개씩 그룹으로 묶어 난이도 계산
    for i in range(0,N,5) :
        group = minerals[i:i+5]
        
        dia = group.count("diamond")
        iron = group.count("iron")
        stone = group.count("stone")
        
        difficulty = dia * 25 + iron * 5 + stone
        
        groups.append((difficulty, dia, iron, stone))
    
    # 난이도 내림차순 정렬
    groups.sort(reverse = True)
    
    # 곡괭이
    pick = 0
    ans = 0
    
    # 난이도 높은 순으로 곡괭이 배정
    for dif, dia, iron, stone in groups :
    
        while pick < 3 and picks[pick] == 0 :
            pick += 1

        if pick == 3 :      # 곡괭이 없음
            break
            
        picks[pick] -= 1
        
        if pick == 0 :
            ans += dia + iron + stone
        
        elif pick == 1 :
            ans += dia * 5 + iron + stone
        
        else :
            ans += dif
    
    return ans
        
        

        
    