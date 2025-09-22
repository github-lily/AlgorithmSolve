import sys
input = sys.stdin.readline

from collections import deque

M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N) ]
v = [[-1]*M for _ in range(N)]
q = deque()

di,dj = [0,-1,0,1],[-1,0,1,0]


for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 1 :
            q.append((i,j))
            v[i][j] = 0

while q :
    ci,cj = q.popleft()

    for k in range(4) :
        ni,nj = ci+di[k] , cj+dj[k]
        if 0<= ni < N and 0 <= nj < M :
            if arr[ni][nj] == 0 and v[ni][nj] == -1 :
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni,nj))


ans = 0
for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 0 :
            if v[i][j] == -1 :
                print(-1)
                sys.exit(0)
            ans = max(ans,v[i][j])

print(ans)        
