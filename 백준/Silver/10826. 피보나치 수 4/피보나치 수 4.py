n = int(input())

# 피보나치 수를 저장할 리스트 (0부터 n까지)
dp = [0] * (n + 1)

if n > 0:
    dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
