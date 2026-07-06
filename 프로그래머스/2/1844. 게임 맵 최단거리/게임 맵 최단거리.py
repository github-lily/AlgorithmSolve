from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    di,dj = [1,0,-1,0],[0,1,0,-1]
    
    visit = [[-1] * m for _ in range(n)]
    q = deque([(0,0)])
    visit[0][0] = 1
    
    while q :
        ci,cj = q.popleft()
        
        if ci == n-1 and cj == m-1 :
            return visit[ci][cj]
        
        for d in range(4) :
            ni,nj = ci + di[d], cj+dj[d]
            if 0<= ni < n and 0<= nj < m and maps[ni][nj] == 1 and visit[ni][nj] == -1 :
                visit[ni][nj] = visit[ci][cj] + 1
                q.append((ni,nj))
    
    return -1