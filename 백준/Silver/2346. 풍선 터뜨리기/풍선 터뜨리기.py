from collections import deque

n = int(input())
moves = list(map(int, input().split()))

# deque에 (풍선 번호, 이동 값) 저장
balloons = deque((i+1, num) for i, num in enumerate(moves))

result = []

while balloons:
    idx, move = balloons.popleft()  # 풍선 터뜨리기
    result.append(idx)

    if not balloons:
        break

    # 회전 방향 처리
    if move > 0:
        balloons.rotate(-(move - 1))  # 오른쪽으로 move-1번 회전
    else:
        balloons.rotate(-move)        # 왼쪽으로 abs(move)번 회전

print(*result)
