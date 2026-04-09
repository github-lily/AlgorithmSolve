# 한칸 아래 이동, 좌, 가운데,우로만 이동 가능
# 같은 방향으로 두번 연속 이동 불가능

# 입력값
N,M = map(int,input().split())
route = [list(map(int,input().split())) for _ in range(N)]


INF = float(1e9)
dj = [-1,0,1]   # 좌, 가운데, 우

# dp[i][j][d] : i,j에 d 방향으로 도착했을 때 최소 비용
dp = [[[INF]*3 for _ in range(M)] for _ in range(N)]   # 추가

# 첫 줄 초기화
for j in range(M):
    for d in range(3):
        dp[0][j][d] = route[0][j]

# 아래로 내려가면서
for i in range(1, N):
    for j in range(M):
        for d in range(3):  # 현재 방향
            pj = j - dj[d]  # 이전 위치

            if 0 <= pj < M:
                for prev_d in range(3):
                    if prev_d != d:   # 같은 방향 금지
                        dp[i][j][d] = min(
                            dp[i][j][d],
                            dp[i-1][pj][prev_d] + route[i][j]
                        )

# 마지막 줄에서 최소
ans = min(min(dp[N-1][j]) for j in range(M))
print(ans)