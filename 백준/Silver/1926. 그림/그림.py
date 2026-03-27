from collections import deque

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

ans = 0
extent = 0

dr,dc = [0,1,0,-1], [1,0,-1,0] # 우하좌상


def bfs(r,c) :
    global paint

    q = deque()
    q.append((r,c))
    arr[r][c] = -1
    paint = 1

    while q :
        cr,cc = q.popleft()

        for k in range(4) :
            nr,nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 :
                arr[nr][nc] = -1
                paint += 1
                q.append((nr,nc))


for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 1 :
            paint = 0
            ans += 1    # 그림 개수 추가
            bfs(i,j)
            if extent < paint :     # 최대 그림 넓이 갱신
                extent = paint  


print(ans)
print(extent)