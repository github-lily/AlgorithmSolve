# 0 : 빈 칸, 6 : 벽
# 1번 한방향, 2번 180도 두방향, 3번 직각 두방향, 4번 3방향, 5번 4방향으로 쭉 감시
# 회전 가능, 대각선 감시 X
# CCTV끼리는 투시 가능


# 최대 감시! = 최소 사각지대!
from copy import deepcopy

def watch(i,j,d,tmp) :
    ni, nj = i,j
    while True :
        ni += di[d]
        nj += dj[d]
        if not (0 <= ni < n and 0 <= nj < m) :
            break
        if tmp[ni][nj] == 6 :
            break
        if tmp[ni][nj] == 0 :
            tmp[ni][nj] = -1


def dfs(cctv_now, arr) :
    global ans
    if cctv_now == len(cctv) :      # cctv 모두 확인하면 종료
        cnt = 0
        for r in range(n) :
            for c in range(m) :
                if arr[r][c] == 0 :
                    cnt += 1
        
        if ans > cnt :
            ans = cnt
        
        return ans

    r,c,cctv_type = cctv[cctv_now]

    for case in cctv_dir[cctv_type] :
        tmp = deepcopy(arr)

        for d in case :
            watch(r,c,d,tmp)

        dfs(cctv_now + 1, tmp)
        


n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

cctv = []
ans = int(1e9)

di, dj = [0,1,0,-1], [1,0,-1,0]
cctv_dir = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]

for i in range(n) :
    for j in range(m) :
        if 1 <= arr[i][j] <= 5 :
            cctv.append((i,j,arr[i][j]))


dfs(0,arr)

print(ans)

