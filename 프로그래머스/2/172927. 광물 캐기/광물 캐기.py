def solution(picks, minerals):
    # 캘 수 있는 광석 수
    can_cnt = sum(picks) * 5
    ans = 0
    
    # 캘 수 있는 광석 만큼만 계산
    if len(minerals) > can_cnt :
        minerals = minerals[:can_cnt]
    
    N = len(minerals)
    # 5개 묶음별 피로도
    gazes = []
    turn = -1
    for i in range(0, N, 5) :
        turn += 1
        gaze = 0
        for j in range(5) :
            if i+j < N:
                mineral = minerals[i+j]
                
                if mineral == 'diamond' :
                    gaze += 25
                elif mineral == 'iron' :
                    gaze += 5
                else :
                    gaze += 1
        

        gazes.append((gaze,turn))
    print(gazes)
        
    # 묶음 난이도가 높은 순으로 정렬
    gazes.sort(reverse = True)
    

    # 곡괭이 별 피로도 계산 
    def cal(gaze, turn) :
        nonlocal picks
        
        total = 0
        
        for i in range(3) :
            if not picks[i] :
                continue
                
            picks[i] -= 1
            
            if i == 0 : # 다이아는 개수만큼만 계산
                start = turn*5
                end = min(start+5, N)
                total = end - start
                
            # 철    
            elif i == 1 :       
                for idx in range(turn*5, turn*5+5) :
                    if idx > N-1 :
                        break
                    if minerals[idx] == 'diamond' :
                        total += 5
                    else :
                        total += 1
                        
            # 돌 = 미리 계산한 값            
            else :  
                total = gaze
            
                    
            return total
                

    # 곡괭이 배정
    for g,t in gazes :
        temp = cal(g,t)
        ans += temp
    
    
    return ans
        
        
                
                
    
    