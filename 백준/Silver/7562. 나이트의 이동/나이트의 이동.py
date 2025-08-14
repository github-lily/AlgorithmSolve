import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for _ in range(T) :
    N = int(input())
    si,sj = map(int,input().split())
    ti,tj = map(int,input().split())

    if si == ti and sj == tj :
        print(0)
        continue
    
    v = [[-1]*N for _ in range(N)]

    q = deque([(si,sj)])
    v[si][sj] = 0       

    d = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
    while q :
        ci,cj = q.popleft()

        if ci == ti and cj == tj :
            print(v[ti][tj])
            break

        for di,dj in d :
            ni,nj = ci+di, cj+dj
            # 범위내, 미방문(deque니까 미방문했다는게 최초경로라는 뜻)
            if 0<= ni < N and 0<= nj < N and  v[ni][nj] == -1  :
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni,nj))