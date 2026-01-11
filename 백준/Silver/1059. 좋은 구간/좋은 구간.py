# BOJ 1059 좋은 구간
# 구현: 정렬 + bisect로 n의 양쪽 경계(low, high) 찾기

import sys
from bisect import bisect_left

def main():
    input = sys.stdin.readline

    L = int(input().strip())
    S = list(map(int, input().split()))
    n = int(input().strip())

    S.sort()

    # n이 집합 S에 포함되면 좋은 구간을 만들 수 없음
    if n in S:
        print(0)
        return

    # high = n보다 큰 가장 작은 S 원소 (문제 제한상 n <= max(S)라서 항상 존재)  # 주석: 근거는 문제 제한
    idx = bisect_left(S, n)
    high = S[idx]

    # low = n보다 작은 가장 큰 S 원소, 없으면 0(양의 정수 조건 때문에 A는 최소 1부터 가능)
    low = S[idx - 1] if idx > 0 else 0

    # (n - low) * (high - n) 에서 A=B=n 한 케이스를 제외하므로 -1
    ans = (n - low) * (high - n) - 1
    print(ans)

if __name__ == "__main__":
    main()
