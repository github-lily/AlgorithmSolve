import sys
input = sys.stdin.readline

from collections import deque

def normal(i,j) :
    global color

    q = deque()
    q.append((i,j))
    v[i][j] = 1



    while q :
        ci,cj = q.popleft()

        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
            ni,nj = ci+di, cj+dj
            # 범위내, 미방문, 같은 색
            if 0<= ni < N and 0<= nj < N and v[ni][nj] == 0 and paint[ni][nj] == color :
                v[ni][nj] = 1
                q.append((ni,nj))


def color_blind(i,j) :
    global blind_color

    q = deque()
    q.append((i,j))
    blind_v[i][j] = 1


    while q :
        ci,cj = q.popleft()

        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
            ni,nj = ci+di, cj+dj
            # 범위내, 미방문
            if 0<= ni < N and 0<= nj < N and blind_v[ni][nj] == 0 :
                # 같은 색
                if paint[ni][nj] == blind_color :
                    blind_v[ni][nj] = 1
                    q.append((ni,nj))
                
                # 같은색이 아니어도 적록색일 경우
                elif blind_color == "R" or blind_color == "G":
                    if paint[ni][nj] == "G" or paint[ni][nj] == "R" :
                        blind_v[ni][nj] = 1
                        q.append((ni,nj))



N = int(input())
paint = [list(input().strip()) for _ in range(N)]   # 문자열 값받기 주의~~


# 영역의 개수
cnt = blind_cnt = 0

# 정상인과 색맹의 방문 배열
v = [[0]*N for _ in range(N)]
blind_v = [[0]*N for _ in range(N)]



for i in range(N) :
    for j in range(N) :
        if v[i][j] == 0 :       # 미방문이라면 영역 탐색
            color = paint[i][j] # 비교용 컬러 저장
            cnt += 1            # 영역 개수 += 1
            normal(i,j)
        
        if blind_v[i][j] == 0 :
            blind_color = paint[i][j]
            blind_cnt += 1
            color_blind(i,j)



print(cnt, blind_cnt)