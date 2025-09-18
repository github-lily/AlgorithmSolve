def solution(m, n, puddles):
    answer = 0
    dp =[[0] * (m+1) for _ in range(n+1)]  # 1-index
    # 웅덩이 표시
    for xj,xi in puddles :
        dp[xi][xj] = -1

    
    dp[1][1] = 1    #시작점부터 1
    for i in range(1,n+1) :
        for j in range(1,m+1) :
            if i == 1 and j == 1 :
                continue
            if dp[i][j] != -1 :
                if dp[i-1][j] == -1 and dp[i][j-1] == -1 :      # 위,왼쪽 모두 막혔다면
                    continue
                elif dp[i-1][j] == -1 :                         # 위만 막혔다면
                    dp[i][j] = dp[i][j-1]  % 1000000007
                elif dp[i][j-1] == -1 :                         # 왼쪽이 막혔다면
                    dp[i][j] = dp[i-1][j]  % 1000000007
                else :
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
        
    answer = dp[n][m]
    return answer