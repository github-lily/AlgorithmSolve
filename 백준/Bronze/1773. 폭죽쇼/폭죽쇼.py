n, c = map(int, input().split())
fireworks = [False] * (c + 1)

for _ in range(n):
    interval = int(input())
    for t in range(interval, c + 1, interval):
        fireworks[t] = True

print(sum(fireworks))
