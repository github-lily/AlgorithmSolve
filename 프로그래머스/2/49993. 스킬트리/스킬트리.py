def solution(skill, skill_trees):
    
    ans = len(skill_trees)
    
    for tree in skill_trees :
        i = 0
        impos = set(skill[1:])
        

        for t in tree :
            # 불가능한게 나오면 ans -1 하고 종료
            if t in impos :
                ans -= 1
                break
            
            # 현재 레벨에 맞는게 나오면 impos에서 제거하고 다음것과 비교
            elif t == skill[i] :
                if i < len(skill)-1  :
                    i += 1
                    impos.discard(skill[i])
                if not impos :
                    break
                
    return ans

            
            