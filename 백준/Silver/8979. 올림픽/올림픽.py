import sys
input = sys.stdin.readline

N, K = map(int, input().split())
medals = {}
for _ in range(N):
    c, g, s, b = map(int, input().split())
    medals[c] = (g, s, b)

kg, ks, kb = medals[K]
rank = 1
for c, (g, s, b) in medals.items():
    if (g, s, b) > (kg, ks, kb):
        rank += 1

print(rank)
