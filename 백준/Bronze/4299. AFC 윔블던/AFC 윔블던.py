import sys
input = sys.stdin.readline

S, D = map(int, input().split())

# 불가능 조건: 합보다 차가 크거나, (S+D)가 홀수인 경우
if S < D or (S + D) % 2 == 1:
    print(-1)
else:
    A = (S + D) // 2
    B = (S - D) // 2
    print(A, B)
