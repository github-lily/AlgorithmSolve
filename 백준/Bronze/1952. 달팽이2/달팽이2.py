import sys
input = sys.stdin.readline


M,N = map(int,input().split())
arr = [[0]*N for _ in range(M)]



di,dj = [0,1,0,-1],[1,0,-1,0]  # 우, 하, 좌, 상
i,j,d = 0,0,0             # 시작점, 방향
arr[0][0] = 1           # 방문 체크
cnt = 0                 # 꺾이는 횟수 카운트(끝에서 하나 추가됨)

for _ in range(M*N-1) : # 이미 방문한 시작칸 제외 모두 돌 수 있도록
    ni,nj = i+di[d], j+dj[d]
    if 0<= ni < M and 0<= nj < N and arr[ni][nj] != 1 : # 범위이내이고 방문한 적 없다면
        arr[ni][nj] = 1     # 방문 체크
        i,j = ni,nj
    
    else :
        d = (d+1) % 4
        cnt += 1
        i += di[d]
        j += dj[d]
        arr[i][j] = 1

    
print(cnt)