# 0 : 빈 칸, 6 : 벽
# 1번 한방향, 2번 180도 두방향, 3번 직각 두방향, 4번 3방향, 5번 4방향으로 쭉 감시
# 회전 가능, 대각선 감시 X
# CCTV끼리는 투시 가능


# 최대 감시! = 최소 사각지대!
from copy import deepcopy

def watch(tmp,i,j,d) :
    ni,nj = i,j
    while True :
        ni += di[d]
        nj += dj[d]
        if not (0 <= ni < n and 0 <= nj < m) :      # 범위 밖
            break
        if tmp[ni][nj] == 6 :       # 벽
            break
        if tmp[ni][nj] == 0 :
            tmp[ni][nj] = -1        # 감시 체크


def dfs(cam_order,arr) :
    global ans
    if cam_order == len(cctv) :
        cnt = 0
        for i in range(n) :
            for j in range(m) :
                if arr[i][j] == 0 :
                    cnt += 1
        if ans > cnt :
            ans = cnt
        return
    
    i,j,cam_type = cctv[cam_order]

    for case in dirs[cam_type] :
        tmp = deepcopy(arr)

        for d in case :
            watch(tmp,i,j,d)
        
        dfs(cam_order+1, tmp)


n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

cctv = []
ans = int(1e9)

di,dj = [0,1,0,-1],[1,0,-1,0]
dirs = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]


for i in range(n) :
    for j in range(m) :
        if arr[i][j] != 0 and arr[i][j] != 6 :
            cctv.append((i,j,arr[i][j]))

dfs(0,arr)

print(ans)


