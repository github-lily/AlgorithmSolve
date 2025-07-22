n = int(input())
scores = list(map(int, input().split()))

total, bonus = 0, 0
for s in scores:
    if s == 1:
        bonus += 1
        total += bonus
    else:
        bonus = 0
print(total)
