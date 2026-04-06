
import sys
input = sys.stdin.readline

N, D = map(int,input().split())
dp = [x for x in range(D+1)]        # 해당 index까지의 최단거리 기록

shortcuts = []
for _ in range(N) :
    s,e,l = map(int,input().split())
    # 도착점이 끝점보다 멀거나, 길이가 원래 이동거리보다 먼 경우 제외
    if e <= D and e-s > l :
        shortcuts.append([s,e,l])
shortcuts.sort()

s_idx = 0

for i in range(D+1) :
    # i를 1부터 시작하면 지름길 시작이 0인경우 체크가 안됨
    if i != 0 :
        if dp[i] > dp[i-1] + 1 :
            dp[i] = dp[i-1] + 1

    # 지름길 체크(같은 시작점이 여러개일 수 있으므로 계속 체크)
    while s_idx < len(shortcuts) and shortcuts[s_idx][0] == i :
        start,end,length = shortcuts[s_idx]
        if end <= D : 
            if dp[end] > dp[i] + length :
                dp[end] = dp[i] + length
        s_idx += 1

print(dp[D])