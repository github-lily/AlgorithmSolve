def solution(n, results):
    arr = [[0]* n for _ in range(n+1)]
    
    for w,l in results :
        arr[w-1][l-1] = 1
    
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if arr[i][j] == 0 and arr[i][k] and arr[k][j] :
                    arr[i][j] = 1
                
    # 등수 알 수 있는 사람 구하기
    r_sum = [0] * n
    c_sum = [0] * n
    for r in range(n) :
        for c in range(n) :
            r_sum[r] += arr[r][c]
            c_sum[c] += arr[r][c]
    
    ans = 0
    for i in range(n) :
        if r_sum[i] + c_sum[i] == n-1 :
            ans += 1
    
            
        
    


    
    return ans
            
    