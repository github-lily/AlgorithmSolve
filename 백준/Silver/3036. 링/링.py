import math

n = int(input())
rings = list(map(int, input().split()))

for i in range(1, n):
    g = math.gcd(rings[0], rings[i])
    print(f"{rings[0]//g}/{rings[i]//g}")
