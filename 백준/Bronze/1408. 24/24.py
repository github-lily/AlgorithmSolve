def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def seconds_to_time(sec):
    h = sec // 3600
    sec %= 3600
    m = sec // 60
    s = sec % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

# 입력 받기
current = list(map(int, input().split(":")))
target = list(map(int, input().split(":")))

# 초 단위로 변환
current_sec = time_to_seconds(*current)
target_sec = time_to_seconds(*target)

# 시간 차이 계산
if target_sec < current_sec:
    target_sec += 24 * 3600  # 다음 날로 간 것으로 간주

diff = target_sec - current_sec

# 결과 출력
print(seconds_to_time(diff))
