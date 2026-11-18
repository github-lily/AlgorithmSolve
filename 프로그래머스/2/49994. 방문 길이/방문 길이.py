def solution(dirs):
    visited = set()
    x, y = 0, 0

    move = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }

    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy

        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue

        # 양방향을 같은 길로 처리하기 위해 정렬
        path = tuple(sorted([(x, y), (nx, ny)]))
        visited.add(path)

        x, y = nx, ny

    return len(visited)