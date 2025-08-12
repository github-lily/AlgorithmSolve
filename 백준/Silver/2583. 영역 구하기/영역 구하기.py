import sys
input = sys.stdin.readline

from collections import deque

def bfs(i,j) :
    global cnt
    q = deque()
    q.append((i,j))
    width = 1           # 시작점포함
    while q :
        ci,cj = q.popleft()

        for di,dj in ((0,1),(1,0),(0,-1),(-1,0))  :
            ni,nj = ci+di, cj+dj
            # 범위내, 미방문, 빈공간
            if 0<= ni < N and 0<= nj < M and v[ni][nj] == 0  :
                v[ni][nj] = 1
                width += 1
                q.append((ni,nj))       # 빈 공간을 모두 1로 바꾼 뒤 q 종료
    return width



M, N, K = map(int,input().split())
v = [[0] * M for _ in range(N)]
# print(v)

for _ in range(K) :
    r1,c1,r2,c2 = map(int,input().split())
    
    # 직사각형 부분에 방문 표시
    # print("**r1:",r1,"r2:",r2,"c1:", c1,"c2:",c2)
    for r in range(r1,r2) :    
        for c in range(c1,c2) :
            # print("r:",r,"c:", c)
            if v[r][c] == 0 :
                v[r][c] = 1


cnt = 0
width_lst = []


for i in range(N) :
    for j in range(M) :
        if v[i][j] == 0 :
            v[i][j] = 1
            cnt += 1

            box_width = bfs(i,j)
            width_lst.append(box_width)




print(cnt)
width_lst.sort()
print(*width_lst)