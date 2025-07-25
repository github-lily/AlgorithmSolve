import sys
input = sys.stdin.readline

N = int(input())
time_table = []
for _ in range(N) :
    s,e = map(int,input().split())
    time_table.append([s,e])

# 종료시간 빠른순 정렬 + 시작순서 빠른순 정렬(시작하자마자 끝나는 경우 고려)
time_table.sort(key = lambda x : (x[1], x[0]))
# print(arr)

k = 0
cnt = 0
for start, end in time_table :
    if start >= k :
        k = end
        cnt += 1


print(cnt)