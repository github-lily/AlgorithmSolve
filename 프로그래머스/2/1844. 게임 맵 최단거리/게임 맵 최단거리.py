from collections import deque

# 시작과 종료 블럭 포함
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    di, dj = [1,0,-1,0],[0,1,0,-1]  # 하우상좌
    v = [[0] * m for _ in range(n)]
    v[0][0] = 1
    q = deque([(0,0,1)])
    
    while q :
        ci,cj,cnt = q.popleft()
        
        if ci == n-1 and cj == m-1 :
            return cnt
        
        for k in range(4) :
            ni,nj = ci+di[k], cj+dj[k]
            if 0<=ni<n and 0<=nj<m and maps[ni][nj] == 1 and v[ni][nj] == 0 :
                q.append((ni,nj,cnt+1))
                v[ni][nj] = 1
    
    return -1

        
    
    
    

    
    
    