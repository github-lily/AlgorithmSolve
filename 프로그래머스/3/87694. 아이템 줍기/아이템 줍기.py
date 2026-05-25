from collections import deque

def solution(rect, ux, uy, ix, iy):
    # ㄷ,ㅁ 경우 고려 2배처리
    arr = [[-1]*102 for _ in range(102)]
    v = [[-1]*102 for _ in range(102)]
    
    di, dj = [0,1,0,-1], [1,0,-1,0]
    
    for r in rect :
        sx,sy,ex,ey = map(lambda x : x*2, r)
        # 내부 빈공간 처리
        for i in range(sy+1,ey) :
            for j in range(sx+1,ex) :
                arr[i][j] = 0
        # 테두리 표시
        for i in range(sy,ey+1) :
            for j in range(sx,ex+1) :
                if arr[i][j] != 0 :
                    arr[i][j] = 1
                    
    
    q = deque([(uy*2, ux*2)])
    v[uy*2][ux*2] = 0
    
    while q :
        ci, cj = q.popleft()
        # 아이템 위치 도착하면 종료
        if ci == iy*2 and cj == ix*2 :
            ans = v[ci][cj] // 2
            return ans
        
        
        for k in range(4) :
            ni,nj = ci+di[k], cj+dj[k]
            if 0 <= ni < 102 and 0 <= nj < 102 :
                if arr[ni][nj] == 1 and v[ni][nj] == -1 :
                    v[ni][nj] = v[ci][cj] + 1       # 지나온 칸 표시
                    q.append((ni,nj))
    

        
