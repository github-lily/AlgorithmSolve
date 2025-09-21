import sys
input = sys.stdin.readline

N = int(input())
stairs = [0]*(N+1)   # 시작점 0
for idx in range(1,N+1) :
    stairs[idx] = int(input())

dp = [0] * (N+1)

if N == 1 :
    print(stairs[1])

else :
    dp[1] = stairs[1]
    dp[2] = dp[1] + stairs[2]
    for i in range(3,N+1) :
        dp[i] = max(dp[i-2],dp[i-3] + stairs[i-1]) + stairs[i]
        # 현재 계단에 오기 위한 조건을 고려한 최대값 계산
        # 현재 계단을 밟으려면 2칸 전 계단을 밟았거나, 3칸전 계단과 이전 계단을 밟아야 함
        # 이전 계단만 보면 연속일 수 있으므로 3칸전 계단도 함께 확인

    print(dp[N])