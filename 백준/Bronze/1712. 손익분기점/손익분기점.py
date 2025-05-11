A, B, C = map(int, input().split())

if C <= B:
    print(-1)
else:
    breakeven = A // (C - B) + 1
    print(breakeven)
