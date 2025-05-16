A, B = input().split()
total = 0

for a in A:
    for b in B:
        total += int(a) * int(b)

print(total)
