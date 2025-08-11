import sys
from collections import deque
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

def count_mass():
    # 현재 빙산 격자에서 연결 덩어리 개수를 BFS로 카운트
    v = [[0]*M for _ in range(N)]
    mass = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if A[i][j] > 0 and not v[i][j]:
                mass += 1
                if mass >= 2:
                    return mass
                q = deque([(i, j)])
                v[i][j] = 1
                while q:
                    ci, cj = q.popleft()
                    for k in range(4):
                        ni, nj = ci+di[k], cj+dj[k]
                        if 0 <= ni < N and 0 <= nj < M and A[ni][nj] > 0 and not v[ni][nj]:
                            v[ni][nj] = 1
                            q.append((ni, nj))
    return mass

def melt_once():
    #한 해 동안 동시에 녹이기 인접 바닷물(0) 개수만큼 감소
    dec = [[0]*M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if A[i][j] > 0:
                cnt0 = 0
                for k in range(4):
                    ni, nj = i+di[k], j+dj[k]
                    if A[ni][nj] == 0:
                        cnt0 += 1
                dec[i][j] = cnt0

    # 동시에 적용
    all_zero = True
    for i in range(1, N-1):
        for j in range(1, M-1):
            if A[i][j] > 0:
                A[i][j] = max(0, A[i][j] - dec[i][j])
            if A[i][j] != 0:
                all_zero = False
    return all_zero  # 전부 녹았는지 여부

year = 0
while True:
    c = count_mass()
    if c >= 2:
        print(year)
        break
    if c == 0:
        print(0)
        break
    # 아직 한 덩어리이면서 남아있다면 한 해 녹인다
    melted_all = melt_once()
    year += 1
