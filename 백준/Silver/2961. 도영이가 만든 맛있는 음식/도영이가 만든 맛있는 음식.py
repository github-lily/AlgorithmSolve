import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [tuple(map(int, input().split())) for _ in range(N)]  # (S, B)

ans = float('inf')
for mask in range(1, 1 << N):           # 공집합 제외
    s_prod = 1
    b_sum = 0
    for i in range(N):
        if mask & (1 << i):
            s, b = arr[i]
            s_prod *= s
            b_sum += b
    ans = min(ans, abs(s_prod - b_sum))

print(ans)
