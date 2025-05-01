import sys
input = sys.stdin.readline

R, C = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(R)]

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
max_cnt = 1

def find(i, j, visited, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < R and 0 <= nj < C:
            char = arr[ni][nj]
            idx = ord(char) - ord('A')  # A=0, B=1, ..., Z=25
            if not (visited & (1 << idx)):  # 아직 방문 안했으면
                find(ni, nj, visited | (1 << idx), cnt + 1)

start_char = arr[0][0]
start_visited = 1 << (ord(start_char) - ord('A'))
find(0, 0, start_visited, 1)
print(max_cnt)
