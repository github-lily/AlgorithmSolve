H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

for row in grid:
    res = []
    last_cloud = -1
    for i in range(W):
        if row[i] == 'c':
            last_cloud = i
            res.append(0)
        else:
            if last_cloud == -1:
                res.append(-1)
            else:
                res.append(i - last_cloud)
    print(' '.join(map(str, res)))
