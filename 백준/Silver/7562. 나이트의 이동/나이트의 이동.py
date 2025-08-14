import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for _ in range(T) :
    N = int(input())
    chess = [[0]*N for _ in range(N)]
    v = [[0]*N for _ in range(N)]

    si,sj = map(int,input().split())
    ti,tj = map(int,input().split())

    q = deque([(si,sj)])
    v[si][sj] = 1       #나중에 -1 해주기

    d = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
    while q :
        ci,cj = q.popleft()

        if ci == ti and cj == tj :
            print(v[ti][tj]-1)
            break

        for di,dj in d :
            ni,nj = ci+di, cj+dj
            # 범위내, 미방문 또는 가중치최소
            if 0<= ni < N and 0<= nj < N and ( v[ni][nj] == 0 or v[ni][nj] > (v[ci][cj]+1)) :
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni,nj))

    
        
    