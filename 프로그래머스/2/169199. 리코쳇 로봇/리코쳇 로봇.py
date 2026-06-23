from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    
    # 시작점 찾기
    def find_start() :
        for i in range(n) :
            for j in range(m) :
                if board[i][j] == 'R' :
                    return i,j
                
    si,sj = find_start()
    di,dj = [0,1,0,-1],[1,0,-1,0]       # 우하좌상
    
    # 최소 이동 찾기
    v = [[False]*m for _ in range(n)]
    q = deque([(si,sj,0)])
    v[si][sj] = True
    
    while q :
        ci,cj,cnt = q.popleft()
        
        if board[ci][cj] == 'G' :
            return cnt
        
        for k in range(4) :
            ti,tj = ci,cj
            
            # 한 방향으로 끝까지 이동
            while True :
                ni,nj = ti + di[k], tj + dj[k]
                
                if not (0<=ni<n) or not (0<= nj < m) or board[ni][nj] == 'D' :   
                    break       # 범위 밖 or 벽이면 멈춤
                
                # 갈 수 있으면 전진
                ti,tj = ni,nj
            
            # 끝까지 이동 후 위치 확인
            if not v[ti][tj] :
                q.append((ti,tj, cnt+1))
                v[ti][tj] = True
                    
    
    return -1
                    
        
        
        
                