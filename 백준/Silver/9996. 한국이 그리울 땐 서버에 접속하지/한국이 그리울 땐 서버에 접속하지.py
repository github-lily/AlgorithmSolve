import sys

input = sys.stdin.readline

n = int(input().strip())
pat = input().strip()
pre, suf = pat.split('*', 1)

for _ in range(n):
    s = input().strip()
    if len(s) < len(pre) + len(suf):
        print("NE")
    elif s.startswith(pre) and s.endswith(suf):
        print("DA")
    else:
        print("NE")
