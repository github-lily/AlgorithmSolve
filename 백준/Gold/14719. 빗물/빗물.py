H,W = map(int,input().split())
walls = list(map(int,input().split()))

ans = 0

for i in range(1,W) :
    left = max(walls[:i])
    right = max(walls[i:])

    water = min(left,right) - walls[i]
    if water < 0 :
        water = 0

    ans += water

print(ans) 