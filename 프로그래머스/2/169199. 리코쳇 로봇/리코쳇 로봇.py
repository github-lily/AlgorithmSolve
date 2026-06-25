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
    sr,sc = find_start()
    
    # 최소 이동 거리 구하기
    def bfs(si,sj) :
        di, dj = [0,1,0,-1],[1,0,-1,0]

        q = deque([(si,sj,0)])
        v = [[False] * m for _ in range(n)]
        v[si][sj] = True

        while q :
            ci,cj,cnt = q.popleft()

            if board[ci][cj] == 'G' :
                return cnt

            for d in range(4) :
                k = 1
                while True :    # 끝까지 이동
                    ni, nj = ci + di[d] * k, cj + dj[d] * k

                    # 벽 만나거나 범위 벗어나면 이전 좌표 저장
                    if not (0 <= ni < n and 0<= nj < m) or board[ni][nj] == 'D' :
                        ni,nj = ci + di[d] * (k-1), cj + dj[d] * (k-1)
                        if not v[ni][nj] :  # 자기자신으로 돌아오는 것 방지
                            v[ni][nj] = True
                            q.append((ni,nj,cnt+1))
                        break

                    k += 1
        
        return -1
    
    ans = bfs(sr,sc)
    
    return ans
                
                
                
    