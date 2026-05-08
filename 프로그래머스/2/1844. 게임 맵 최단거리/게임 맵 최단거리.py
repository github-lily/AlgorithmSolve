from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    di,dj = [0,1,0,-1],[1,0,-1,0]
    
    v = [[0] * m for _ in range(n)]
    q = deque([(0,0,0)])

    v[0][0] = 1
    
    while q :
        ci,cj,cnt = q.popleft()
        cnt += 1
        if ci == n-1 and cj == m-1 :
            return cnt
        for k in range(4)  :
            ni,nj = ci + di[k], cj + dj[k]
            if 0<= ni < n and 0<= nj < m :
                if v[ni][nj] == 0 and maps[ni][nj] == 1:
                    q.append((ni,nj,cnt))
                    v[ni][nj] = 1
                    
    return -1