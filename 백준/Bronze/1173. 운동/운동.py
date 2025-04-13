N, m, M, T, R = map(int, input().split())

# 운동을 절대 못 하는 경우
if m + T > M:
    print(-1)
else:
    now = m          # 현재 맥박
    time = 0         # 총 경과 시간
    exercise = 0     # 누적 운동 시간

    while exercise < N:
        if now + T <= M:
            # 운동 가능
            now += T
            exercise += 1
        else:
            # 휴식
            now -= R
            if now < m:
                now = m
        time += 1

    print(time)
