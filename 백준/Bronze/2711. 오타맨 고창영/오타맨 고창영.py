T = int(input())
for _ in range(T):
    n, s = input().split()
    n = int(n)
    print(s[:n-1] + s[n:])
