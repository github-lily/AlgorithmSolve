from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # ㄹ, ㅁ 고려하여 x2 하기
    X,Y = 102,102
    arr = [[0]*X for _ in range(Y)]
    
    # 지도에 사각형 그리기(테두리 1, 속은 0)
    for rec in rectangle :
        x1, y1, x2, y2 = [x*2 for x in rec]
        
        for x in range(x1, x2+1) :
            for y in range(y1,y2+1) :
                if x in (x1,x2) or y in (y1,y2) :
                    if arr[x][y] != 2 :
                        arr[x][y] = 1   # 테두리는 1
                else :
                    arr[x][y] = 2   # 속은 2
    
    
    # 가장 짧은 거리 구하기
    dx, dy = [0,1,0,-1], [1,0,-1,0]
    q = deque([(characterX*2, characterY*2, 0)])
    v = [[False]*X for _ in range(Y)]
    v[characterX*2][characterY*2] = True
    
    
    
    while q :
        cx,cy,cnt = q.popleft()
        
        if cx == itemX*2 and cy == itemY*2 :
            return cnt // 2
        
        for k in range(4) :
            nx,ny = cx + dx[k], cy+dy[k]
            if 0 <= nx < X and 0<= ny < Y and arr[nx][ny] == 1 and not v[nx][ny] :
                v[nx][ny] = True
                q.append((nx,ny,cnt+1))
    
    return cnt
        
        
    