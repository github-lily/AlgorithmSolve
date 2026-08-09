from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])

    # 시작점 찾기
    def find_start(n, m):
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'R':
                    return i, j

    si, sj = find_start(n, m)

    di,dj = [1, 0, -1, 0], [0, 1, 0, -1]

    def find_goal(si, sj):
        q = deque([(si, sj, 0)])
        v = [[0] * m for _ in range(n)]
        v[si][sj] = 1

        while q:
            ci, cj, cnt = q.popleft()

            if board[ci][cj] == 'G':
                return cnt

            for d in range(4):
                ni, nj = ci, cj

                # 벽이나 범위 밖 직전까지 이동
                while True:
                    next_i = ni + di[d]
                    next_j = nj + dj[d]

                    if (
                        next_i < 0 or next_i >= n
                        or next_j < 0 or next_j >= m
                        or board[next_i][next_j] == 'D'
                    ):
                        break

                    ni, nj = next_i, next_j

                # 멈춘 위치에 대해서만 방문 체크
                if v[ni][nj] == 0:
                    v[ni][nj] = 1
                    q.append((ni, nj, cnt + 1))

        return -1

    return find_goal(si, sj)