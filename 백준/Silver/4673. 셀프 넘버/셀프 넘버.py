def d(n):
    return n + sum(map(int, str(n)))

self_numbers = set(range(1, 10001))
for i in range(1, 10001):
    self_numbers.discard(d(i))

for num in sorted(self_numbers):
    print(num)
