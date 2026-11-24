def solution(land):
    N = len(land)

    for i in range(1, N):
        for j in range(4):
            mx = 0

            # 이전 행에서 현재 열을 제외한 최대 점수 탐색
            for k in range(4):
                if j == k:
                    continue

                mx = max(mx, land[i-1][k])

            # 현재 점수에 이전 행의 최대 누적 점수 더하기
            land[i][j] += mx

    # 마지막 행에서 최대 누적 점수 반환
    return max(land[N-1])