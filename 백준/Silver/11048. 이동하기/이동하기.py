
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [0] * (M+1)


for i in range(N) :
    for j in range(1,M+1) :
        dp[j] = max(dp[j-1]+arr[i][j-1], dp[j]+arr[i][j-1])

print(dp[M])
        