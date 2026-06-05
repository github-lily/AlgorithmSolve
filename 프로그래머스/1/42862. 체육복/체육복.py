def solution(n, lost, reserve):
    lst = [1] * (n+2)
        
    # 잃어버린거 체크
    for l in lost :
        lst[l] -= 1
    
    # 여벌 체크
    for r in reserve :
        lst[r] += 1
    
    ans = 0
    for i in range(1, n+1) :
        if lst[i] == 1 :
            ans += 1        # 본인 것만 있으면 넘어감   
        # 여분 있을 때
        elif lst[i] > 1 :
            # 이전 사람이 체육복 없다면
            if i != 1 and lst[i-1] == 0 :
                lst[i] -= 1
                lst[i-1] += 1
                ans += 1
            # 뒷 사람이 체육복 없다면
            if i != n+1 and lst [i] > 1 :
                if lst[i+1] == 0 :
                    lst[i] -= 1
                    lst[i+1] += 1
            ans += 1
        else :
            continue
    
    return ans
        