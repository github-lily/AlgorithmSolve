n = int(input())
count = 0

for i in range(1, n + 1):
    if i < 100:
        count += 1
    else:
        digits = list(map(int, str(i)))
        if digits[0] - digits[1] == digits[1] - digits[2]:
            count += 1

print(count)
