import sys

tokens = list(map(int, sys.stdin.read().split()))
it = iter(tokens)

t = next(it)  # 테스트 케이스 수
out = []

for _ in range(t):
    n = next(it); m = next(it)
    sejun = [next(it) for _ in range(n)]
    sebi  = [next(it) for _ in range(m)]
    if max(sejun) >= max(sebi):
        out.append("S")
    else:
        out.append("B")

print("\n".join(out))
