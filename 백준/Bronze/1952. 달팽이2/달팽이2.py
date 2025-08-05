M, N = map(int, input().split())

# 표 생성 및 방문 체크
visited = [[False] * N for _ in range(M)]
# 방향: → ↓ ← ↑
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y, d = 0, 0, 0  # 시작 좌표와 방향
visited[x][y] = True
turns = 0

for _ in range(M * N - 1):  # 시작 칸은 이미 방문했으므로 -1
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
        x, y = nx, ny
        visited[x][y] = True
    else:
        # 방향 전환
        d = (d + 1) % 4
        turns += 1
        x += dx[d]
        y += dy[d]
        visited[x][y] = True

print(turns)
