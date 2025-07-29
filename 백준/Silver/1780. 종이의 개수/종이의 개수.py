import sys
input = sys.stdin.readline

# 결과 저장용 변수
count = [0, 0, 0]  # index 0: -1, index 1: 0, index 2: 1

def is_same(x, y, size):
    num = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != num:
                return False
    return True

def divide(x, y, size):
    if is_same(x, y, size):
        count[paper[x][y] + 1] += 1  # -1 → 0, 0 → 1, 1 → 2
        return

    new_size = size // 3
    for dx in range(3):
        for dy in range(3):
            nx = x + dx * new_size
            ny = y + dy * new_size
            divide(nx, ny, new_size)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]


divide(0, 0, N)


for c in count:
    print(c)
