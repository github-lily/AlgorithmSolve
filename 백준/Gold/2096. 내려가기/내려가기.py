import sys
input = sys.stdin.readline

N = int(input())
first = list(map(int, input().split()))

# 최대/최소 dp 배열 초기화
max_dp = first[:]
min_dp = first[:]

for _ in range(N - 1):
    a, b, c = map(int, input().split())

    # 이전 상태 보존
    prev_max = max_dp[:]
    prev_min = min_dp[:]

    # 최대값 갱신
    max_dp[0] = a + max(prev_max[0], prev_max[1])
    max_dp[1] = b + max(prev_max[0], prev_max[1], prev_max[2])
    max_dp[2] = c + max(prev_max[1], prev_max[2])

    # 최소값 갱신
    min_dp[0] = a + min(prev_min[0], prev_min[1])
    min_dp[1] = b + min(prev_min[0], prev_min[1], prev_min[2])
    min_dp[2] = c + min(prev_min[1], prev_min[2])

print(max(max_dp), min(min_dp))
