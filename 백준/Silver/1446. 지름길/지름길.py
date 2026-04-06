import sys
input = sys.stdin.readline

N, D = map(int,input().split())
dp = [x for x in range(D+1)]        # 해당 index까지의 최단거리 기록

shortcuts = [list(map(int,input().split())) for _ in range(N)]
shortcuts.sort()

s = 0

for i in range(D+1) :
    # i를 1부터 시작하면 지름길 시작이 0인경우 체크가 안됨
    if i != 0 :
        if dp[i] > dp[i-1] + 1 :
            dp[i] = dp[i-1] + 1

    # 지름길 체크(같은 시작점이 여러개일 수 있으므로 계속 체크)
    while s < len(shortcuts) and shortcuts[s][0] == i :
        start,end,length = shortcuts[s]
        if end <= D : 
            if dp[end] > dp[i] + length :
                dp[end] = dp[i] + length
        s += 1

print(dp[D])