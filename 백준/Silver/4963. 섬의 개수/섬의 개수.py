import sys
input = sys.stdin.readline

from collections import deque

# 대각선 포함 8방향
dr,dc = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]


def bfs(r,c) :
    q = deque([(r,c)])
    v[r][c] = 1

    
    while q :
        cr,cc = q.popleft()
        for k in range(8) :
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < h and 0 <= nc < w :
                if guidance[nr][nc] == 1 and v[nr][nc] == 0 :
                    v[nr][nc] = 1
                    q.append((nr,nc))        
    


while True :
    w,h = map(int,input().split())
    cnt = 0

    # 입력 종료
    if w == 0 and h == 0 :
        break

    guidance = [list(map(int,input().split())) for _ in range(h)]
    v = [[0] * w for _ in range(h)]


    for r in range(h) :
        for c in range(w) :
            if guidance[r][c] == 1 and v[r][c] == 0 :
                bfs(r,c)
                cnt += 1

    print(cnt)

