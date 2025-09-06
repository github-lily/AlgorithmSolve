import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int,input().split()))   # 1번부터

dp = [0] * (N+1)

for i in range(1,N+1) :     # 카드 목표
    max_val = 0
    for j in range(1,i+1) : # 고르는 팩의 크기
        max_val = max(max_val, dp[i-j] + P[j])
    dp[i] = max_val

print(dp[N])
        