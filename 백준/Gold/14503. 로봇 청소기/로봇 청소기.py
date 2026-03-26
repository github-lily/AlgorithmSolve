N,M = map(int,input().split())
si,sj,sd = map(int,input().split()) # sd는 북동남서(시계)

# 북동남서(시계)
di, dj = [-1,0,1,0],[0,1,0,-1]

arr = [list(map(int,input().split())) for _ in range(N)]
cnt  = 0


def clean(ci,cj,cd) :     # 현재 위치(ci,cj)와 방향(cd)
    global cnt

    # 1. 빈칸이면 청소
    if arr[ci][cj] == 0 :
        arr[ci][cj] = -1        # 청소 칸 : -1
        cnt += 1

    # 3. 청소 칸 탐색
    for _ in range(4) :
        cd = (cd+3) % 4         # 반시계 방향으로 90도 회전
        ni, nj =  ci+di[cd], cj+dj[cd]      # 전진

        if 0 <= ni < N and 0 <= nj < M :
            if arr[ni][nj] == 0  :
                clean(ni,nj,cd)
                return          # 돌아와서 다시 for문 돌지 않도록 전진하면 끝!
            
    # 2. 청소할 곳 없을 때
    bi,bj = ci+di[(cd+2)% 4], cj+dj[(cd+2)% 4]  # back 후진
    if 0 <= bi < N and 0 <= bj < M :
        if arr[bi][bj] == 1 :
            return
        else :
            clean(bi,bj,cd)       # 방향 유지

clean(si,sj,sd)

print(cnt)
        
        
        