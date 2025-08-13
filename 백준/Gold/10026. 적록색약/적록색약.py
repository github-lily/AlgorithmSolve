import sys
input = sys.stdin.readline

from collections import deque

def bfs(N,arr) :
    cnt = 0             # 영역의 개수
    v = [[0]*N for _ in range(N)]

    for i in range(N) :
        for j in range(N) :
            if v[i][j] == 0 :       # 미방문이라면 영역 탐색
                color = arr[i][j] # 비교용 컬러 저장
                cnt += 1            # 영역 개수 += 1

                q = deque()
                q.append((i,j))
                v[i][j] = 1

                while q :
                    ci,cj = q.popleft()

                    for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
                        ni,nj = ci+di, cj+dj
                        # 범위내, 미방문, 같은 색
                        if 0<= ni < N and 0<= nj < N and v[ni][nj] == 0 and arr[ni][nj] == color :
                            v[ni][nj] = 1
                            q.append((ni,nj))
    
    return cnt



N = int(input())

# 문자열 각각을 받는 방법
# paint = [list(input().strip()) for _ in range(N)]  

# 문자열을 리스트로 쪼개지 않고 그대로 받는 방법
paint = [input().strip() for _ in range(N)]     # ['RRRBB', 'GGBBB', 'BBBRR', 'BBRRR', 'RRRRR']


normal_cnt = bfs(N,paint)
blind_cnt = bfs(N, [i.replace('R','G') for i in paint])

    
print(normal_cnt, blind_cnt)