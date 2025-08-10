import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
max_cnt = 0

di,dj = [0,1,0,-1],[1,0,-1,0]   # 우하좌상

for h in range(101) :       # 안전영역 높이 1~100
    v = [[0]*N for _ in range(N)]
    cnt = 0                     # 안전영역 개수
    for i in range(N) :
        for j in range(N) :
            if v[i][j] == 0 and arr[i][j] > h :
                v[i][j] = 1
                cnt += 1
                
                q = deque()
                q.append((i,j))

                while q :
                    ci,cj = q.popleft()

                    for k in range(4) :
                        ni,nj = ci+di[k], cj+dj[k]
                        # 범위 내, 미방문, 높이 이상
                        if 0<= ni < N and 0<= nj < N and v[ni][nj] == 0 and arr[ni][nj] > h :
                            v[ni][nj] = 1
                            q.append((ni,nj))

    if max_cnt < cnt :
        max_cnt = cnt

print(max_cnt)


