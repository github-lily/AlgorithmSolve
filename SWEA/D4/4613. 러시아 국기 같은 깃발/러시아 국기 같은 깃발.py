T = int(input())

for t in range(T) :
    N, M = map(int,input().split())
    
    arr = [input() for _ in range(N)]
    
    cost = [[0]*3 for _ in range(N)]

    # 교체비용 구하기
    for i in range(N) :

        w_cnt = 0
        b_cnt = 0
        r_cnt = 0

        for j in range(M) :
            if arr[i][j] == 'W' :
                w_cnt += 1
            elif arr[i][j] == 'B' :
                b_cnt += 1
            elif arr[i][j] == 'R' :
                r_cnt += 1
        
        cost[i][0] = M - w_cnt
        cost[i][1] = M - b_cnt
        cost[i][2] = M - r_cnt
    
    # 범위 조절하며 최소값 찾기
    mx = 9999999999
    for b_start in range(1,N-1) :     
        for r_start in range(b_start+1,N) :
            temp = 0
            
            for k in range(b_start) :
                temp += cost[k][0]
            
            for k in range(b_start,r_start) :
                temp += cost[k][1]
            
            for k in range(r_start, N) :
                temp += cost[k][2]
        
            mx = min(temp,mx)
    
    print(f'#{t+1} {mx}')

