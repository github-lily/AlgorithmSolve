import math

a, b = map(int, input().split(":"))
g = math.gcd(a, b)
print(f"{a // g}:{b // g}")
