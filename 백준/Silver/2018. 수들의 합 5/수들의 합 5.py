import sys
input = sys.stdin.readline

N = int(input().strip())

start, end = 1, 1
cur_sum = 1
cnt = 0

while start <= N:
    if cur_sum == N:
        cnt += 1
        end += 1
        cur_sum += end
    elif cur_sum < N:
        end += 1
        cur_sum += end
    else:  # cur_sum > N
        cur_sum -= start
        start += 1

print(cnt)
