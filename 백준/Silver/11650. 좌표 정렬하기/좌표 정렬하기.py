N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]


for line in sorted(lst) :
    print(*line)