import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    a = sorted(map(int, input().split()))
    ans = 0
    for i in range(2, N):
        ans = max(ans, a[i] - a[i-2])   
    print(ans)
