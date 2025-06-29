R, C = map(int, input().split())
castle = [input().strip() for _ in range(R)]

empty_rows = 0
empty_cols = 0

# 빈 행 세기
for row in castle:
    if 'X' not in row:
        empty_rows += 1

# 빈 열 세기
for col in zip(*castle):
    if 'X' not in col:
        empty_cols += 1

print(max(empty_rows, empty_cols))
