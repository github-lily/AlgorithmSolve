from collections import deque

def bfs(si,sj) :
    q = deque([(si,sj)])

    while q :
        ci,cj = q.popleft()

        if ci == N-1 and cj == M-1 :
            return 

        for k in range(4) :
            ni,nj = ci+di[k], cj+dj[k]
            if 0 <= ni < N and 0 <= nj < M and miro[ni][nj] == 1 :
                miro[ni][nj] = miro[ci][cj]+1
                q.append((ni,nj))
    

N, M = map(int,input().split())
miro = [list(map(int,input())) for _ in range(N)]
di,dj = [0,1,0,-1],[1,0,-1,0]   # 우하좌상

bfs(0,0)

print(miro[N-1][M-1])
