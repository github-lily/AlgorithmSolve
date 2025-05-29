N = int(input())
data = list(map(int, input().split()))

line = [0] * N  # 결과를 담을 줄

for i in range(N):
    cnt = 0
    for j in range(N):
        if line[j] == 0:  # 아직 아무도 안 선 자리일 때만
            if cnt == data[i]:
                line[j] = i + 1  # i+1번 사람(키가 i+1인 사람)을 j자리에 세움
                break
            cnt += 1

print(*line)
