#  |r1 - r2| + |c1 - c2|  > 2 이상이어야 앉을 수 있음
# 파티션으로 막힌 자리는 가능

def solution(places):
    n,m = 5,5       # places 행렬 길이
    di,dj = [0,1,0,-1],[1,0,-1,0]
    ans = []

    def check(arr) :
        for i in range(n) :
            for j in range(m) :
                if arr[i][j] != 'P' :
                    continue
                
                # 사람을 찾으면 상하좌우 확인
                for d in range(4) :
                    ni,nj = i + di[d] , j + dj[d]
                    
                    if not (0 <= ni < n and 0 <= nj < m) :
                        continue

                    # 1. 사람 : 실패
                    if arr[ni][nj] == 'P' :
                        return False

                    # 2. 칸막이 : 그 방향으로는 확인 필요 없음
                    if arr[ni][nj] == 'X' :
                        continue

                    # 3. 테이블 : 테이블의 상하좌우 확인
                    if arr[ni][nj] == 'O' :
                        # 테이블 주변에 사람있으면 실패
                        for od in range(4) :
                            oni,onj = ni + di[od], nj + dj[od]
                            
                            if not (0 <= oni < n and 0<= onj < m) :
                                continue
                            
                            # 자기 자신 제외
                            if oni == i and onj == j:   
                                continue
                                
                            if arr[oni][onj] == 'P' :
                                return False

        return True
                            
                            
                                
    for place in places :
        if check(place) :
            ans.append(1)
        else :
            ans.append(0)
            
    return ans
