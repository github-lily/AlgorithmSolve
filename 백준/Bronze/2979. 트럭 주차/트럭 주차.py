import sys

A, B, C = map(int, sys.stdin.readline().split())

times = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

# 시간은 1~100 사이라 충분히 작은 범위 → 배열로 시간대 전체 체크
parking = [0] * 101

# 각 트럭의 주차 구간을 모두 카운트
for start, end in times:
    for t in range(start, end):  # end 시간은 포함되지 않음
        parking[t] += 1

total_fee = 0
for cnt in parking:
    if cnt == 1:
        total_fee += A
    elif cnt == 2:
        total_fee += B * 2
    elif cnt == 3:
        total_fee += C * 3

print(total_fee)
