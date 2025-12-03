import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
campus = [list(input().strip()) for _ in range(n)]

# 시작점 찾기
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            sx, sy = i, j

visited = [[False]*m for _ in range(n)]
q = deque([(sx, sy)])
visited[sx][sy] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0

while q:
    x, y = q.popleft()

    if campus[x][y] == 'P':
        cnt += 1

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and campus[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append((nx, ny))

print(cnt if cnt > 0 else "TT")
