from collections import deque

# 시작과 종료 블럭 포함
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    def bfs(si,sj) :
        di, dj = [1,0,-1,0],[0,1,0,-1]  # 하우상좌
        v = [[0] * m for _ in range(n)]
        v[si][sj] = 1
        q = deque([(si,sj)])
        cnt = 0
        
        while q :
            ci,cj = q.popleft()
            
            # 도착시 종료
            if ci == n-1 and cj == m-1 :
                return v[ci][cj]

            for k in range(4) :
                ni,nj = ci+di[k], cj+dj[k]
                # 범위 내 & 벽 아님
                if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] == 1 :
                    # 방문 안함 or 더 가까운 경로일 떄 이동
                    if v[ni][nj] == 0 or v[ni][nj] > v[ci][cj] + 1 :
                        q.append((ni,nj))
                        v[ni][nj] = v[ci][cj] + 1
        return -1
        
                
    ans = bfs(0,0)
    
    return ans

    
    

    
    
    