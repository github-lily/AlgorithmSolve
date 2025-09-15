m = int(input())
n = int(input())

primes = []
for num in range(m, n+1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)
