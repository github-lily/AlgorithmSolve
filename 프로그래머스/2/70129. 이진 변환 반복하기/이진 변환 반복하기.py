def solution(s):

    
    total = 0
    zero = 0
    loop = 0

            
    while s != "1" :
        
        N = len(s)     
        loop += 1
        
        # 0 제거
        for num in s :
            if num == "0" : 
                zero += 1
        total += zero
        
        # 2진법 변환
        cnt = N-zero    # 1의 개수
        s = str(bin(cnt)[2:])

        
        # 0 카운트 초기화
        zero = 0
        
        
        
    return loop, total

        
        
        