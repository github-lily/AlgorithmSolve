
import sys
input = sys.stdin.readline

F,S,G,U,D = map(int,input().split())
cnt = 0

while cnt <= 2000000 :
    if S == G :
        print(cnt)
        exit()
    
    cnt += 1

    # 현재 위치가 목표보다 높거나, S+U가 전체 층수보다 높거나, S-D가 1층 이상일 때
    if (S>G or S+U > F) and S-D > 0 :
        if D == 0 :
            break
        S -= D      # D층만큼 아래로

    else :
        S += U      # 위 경우가 아니면 위로
    
    if S > F :
        break       # 만약 현 위치가 전체 층수보다 높으면 멈춤

print("use the stairs")
