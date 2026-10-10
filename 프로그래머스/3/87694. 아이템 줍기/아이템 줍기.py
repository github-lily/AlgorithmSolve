from collections import deque

def solution(rectangles, characterX, characterY, itemX, itemY):
    
    # 지도에 영역 표시
    arr = [[0] * 101 for _ in range(101)]
    
    for rec in rectangles :
        # ㄷ,ㄹ 대비 *2 크기로 그리기
        x1,y1,x2,y2 = [r*2 for r in rec]
        
        for i in range(x1, x2+1) :
            for j in range(y1, y2+1) :
                
                # 테두리 표시
                if arr[i][j] != -1 and (i == x1 or i == x2 or j == y1 or j == y2) :   
                    arr[i][j] = 1
                    
                # 내부는 방문 불가
                else :
                    arr[i][j] = -1
    

    
    # 최단거리 찾기
    q = deque([(characterX*2, characterY*2,0)])
    v = [[0] * 101 for _ in range(101)]
    v[characterX*2][characterY*2] = 1
    
    di, dj = [-1,0,1,0], [0,1,0,-1]
    
    while q :
        ci, cj, cnt = q.popleft()
        
        if ci == itemX*2 and cj == itemY*2 :
            return cnt //2
        
        for d in range(4) :
            ni,nj = ci + di[d] , cj + dj[d]
            if 0 <= ni < 101 and 0 <= nj < 101 :
                if arr[ni][nj] == 1 and v[ni][nj] == 0 :
                    q.append((ni, nj, cnt + 1))
                    v[ni][nj] = 1
                    
            
            
    
    return cnt //2
    
    
                    
    