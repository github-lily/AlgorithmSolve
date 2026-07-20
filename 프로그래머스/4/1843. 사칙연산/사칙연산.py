def solution(arr):
    n = len(arr)//2 + 1
    nums = []
    signs = []
    
    mx_dp = [[float('-inf')] * n for _ in range(n)]
    mn_dp = [[float('inf')] * n for _ in range(n)]
    
    for a in arr :
        if a.isdigit() :
            nums.append(int(a))
        else :
            signs.append(a)
    
    # 길이 1 (자기 자신)
    for i in range(n) :
        mx_dp[i][i] = nums[i]
        mn_dp[i][i] = nums[i]

    # 구간 길이 2부터 n까지
    for lenn in range(2,n+1) :
        
        # 시작점
        for i in range(n - lenn + 1) :
            j = i+lenn-1        # 구간 끝
            
            # 구간 나눠서 누적합으로 계산
            for k in range(i,j) :
                if signs[k] == '+' :
                    mx = mx_dp[i][k] + mx_dp[k+1][j]
                    mn = mn_dp[i][k] + mx_dp[k+1][j]
                
                else :  
                    mx = mx_dp[i][k] - mn_dp[k+1][j]    # 최댓값 만들기
                    mn = mn_dp[i][k] - mx_dp[k+1][j]    # 최솟값 만들기
                    
            
                mx_dp[i][j] = max(mx_dp[i][j], mx)
                mn_dp[i][j] = min(mn_dp[i][j], mn)
    
    return mx_dp[0][n-1]
                    
    
    
    
                
            
    
    
    