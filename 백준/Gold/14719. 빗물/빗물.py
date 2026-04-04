H,W = map(int,input().split())
walls = list(map(int,input().split()))

ans = 0
l,r = 0, W-1
l_mx, r_mx = 0,0

while l < r :
    if walls[l] < walls[r] :        # 더 낮은 왼쪽 벽이 기준
        if walls[l] > l_mx :
            l_mx = walls[l]         # 왼쪽 벽 갱신
        else :
            ans += l_mx - walls[l]
        l += 1
    else :      # 더 낮은 오른쪽 벽이 기준
        if walls[r] > r_mx :
            r_mx = walls[r]         # 오른쪽 벽 갱신
        else :
            ans += r_mx - walls[r]
        r -= 1

print(ans)
