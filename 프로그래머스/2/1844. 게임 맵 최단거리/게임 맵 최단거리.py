from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    si, sj = 0,0
    q = deque([(si,sj)])
    
    v = [[0] * m for _ in range(n)]
    v[0][0] = 1
    
    di,dj = [0,1,0,-1],[1,0,-1,0]
    
    
    while q :
        ci,cj = q.popleft()
        
        if ci == n-1 and cj == m-1 :
            return v[ci][cj]
        
        for d in range(4) :
            ni,nj = ci + di[d], cj + dj[d]
            if 0 <= ni < n and 0 <= nj < m :
                if maps[ni][nj] == 1 and v[ni][nj] == 0 :
                    v[ni][nj] = v[ci][cj] + 1
                    q.append((ni,nj))
        
        
    return -1 
        

    
    