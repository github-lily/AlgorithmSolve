def solution(origin):
    mn = int(1e9)
    n = len(origin)
    
    if n == 1 :
        return 1
    
    temp = ""
    for k in range(1,n//2+1) :
        # k개씩 단어 자르기
        
        target = origin[0:k]
        i = k
        cnt = 1
        temp = ""
        
        while i < n :
            cur = origin[i:i+k]
            # <불일치>
            if target != cur :
                # 이전까지의 값 추가, 타겟 변경, cnt 초기화, i이동
                if cnt == 1 :
                    temp += target
                else :
                    temp += str(cnt) + target
                target = cur
                cnt = 1
                i += k
                # i+k >= n 이라면 종료이므로 값 추가 후 종료
                if i >= n :
                    temp += cur
                    

            # <일치>
            else :
                # cnt 증가, i 이동
                cnt += 1
                i += k
                
                # i+k >= n 이라면 종료이므로 값 추가 후 종료
                if i >= n :
                    temp += str(cnt) + cur
                    
        l = len(temp)
        
        if mn > l :
            mn = l
    
    return mn
                
                
                
    