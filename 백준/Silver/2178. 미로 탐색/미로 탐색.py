from collections import deque

def bfs(si,sj,scnt) :
    q = deque([(si,sj,scnt)])
    miro[si][sj] = 0

    while q :
        ci,cj,cnt = q.popleft()

        if ci == N-1 and cj == M-1 :
            return cnt

        for k in range(4) :
            ni,nj = ci+di[k], cj+dj[k]
            if 0 <= ni < N and 0 <= nj < M and miro[ni][nj] == 1 :
                miro[ni][nj] = 0
                q.append((ni,nj,cnt+1))
    

N, M = map(int,input().split())
miro = [list(map(int,input())) for _ in range(N)]
di,dj = [0,1,0,-1],[1,0,-1,0]   # 우하좌상

ans = bfs(0,0,1)

print(ans)
