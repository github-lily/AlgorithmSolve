N = int(input())
channels = [input() for _ in range(N)]

ans = ""

# 1. KBS1 찾기
idx1 = channels.index("KBS1")
ans += "1" * idx1
ans += "4" * idx1

for i in range(idx1, 0, -1):
    channels[i], channels[i-1] = channels[i-1], channels[i]

# 2. KBS2 찾기
idx2 = channels.index("KBS2")
ans += "1" * idx2
ans += "4" * (idx2 - 1)

print(ans)