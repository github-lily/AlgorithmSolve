def solution(n):
    # 종료 개수 구하기 (등차수열의 합)
    end = n * (n+1) // 2
    
    
    # 기본값 설정
    arr = [[0]*n for _ in range(n)]
    di,dj = [1,0,-1],[0,1,-1]       # 하, 우, 좌상대각선 3방향
    
    num = 1
    d = 0
    ci,cj = 0,0
    
    arr[ci][cj] = num
    num += 1

    
    # 배열 순회
    while num <= end :
        ni, nj = ci + di[d], cj + dj[d]
        
        if 0 <= ni < n and 0<= nj < n and arr[ni][nj] == 0 :
            arr[ni][nj] = num
            num += 1
            ci,cj = ni,nj
        else :
            d = (d + 1) % 3
    
    
    
    # 답
    ans = []
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] != 0 :
                ans.append(arr[i][j])
    
    return ans
    
