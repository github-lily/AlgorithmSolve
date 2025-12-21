import sys

input = sys.stdin.readline

N, M = map(int, input().split())

package = []
single = []

for _ in range(M):
    p, s = map(int, input().split())
    package.append(p)
    single.append(s)

min_package = min(package)
min_single = min(single)

cost = 0

# 패키지로만 사는 경우
cost = min_package * (N // 6)

# 나머지 줄 처리
remain = N % 6
cost += min(min_package, min_single * remain)

# 전부 낱개로 사는 경우와 비교
cost = min(cost, min_single * N)

print(cost)
