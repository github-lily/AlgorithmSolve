def solution(park, routes):
    N = len(park)
    M = len(park[0])
    
    # 시작점 찾기
    for i in range(N) :
        for j in range(M) :
            if park[i][j] == 'S' :
                si, sj = i, j
    
    # 산책 시작
    directs = ["E","S","W","N"]
    di, dj = [0,1,0,-1], [1,0,-1,0] # ESWN
    
    def check(ci,cj,d,n) :
        for k in range(1, n+1) :
            ni,nj = ci+di[d]*k, cj+dj[d]*k
            if not 0<= ni < N or not 0<= nj < M or park[ni][nj] == "X" :
                return ci,cj

        return ni,nj
    
    for route in routes :
        direct, num = route.split()
        num = int(num)
        op = directs.index(direct)
        si,sj = check(si,sj,op,num)
        

    # 세로, 가로 좌표로 return
    return [si,sj]
            
        
        
    
    

    
    
