def solution(N, number):
    dp = [set() for _ in range(8)]      # 만들 수 있는 숫자 집합
    ans = -1
    
    if number == N :
        return 1
    
    # N * i 값 채우기
    for i in range(8) :
        dp[i].add(int(str(N)*(i+1)))
    
    # 만들 수 있는 숫자 집합 계산
    # ex) 3개 : NNN, 1개+2개 사칙연산 값
    # 즉 k = i + j
    for i in range(8) :
        for j in range(i) :     
            for op1 in dp[j] :
                for op2 in dp[i-j-1] :
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 :        # 0이 아닐때만 나눗셈
                        dp[i].add(op1 // op2)
    
        if number in dp[i] :
            return i+1
    
    
    return ans
        
                    
            