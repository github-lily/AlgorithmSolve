T = int(input())
for _ in range(T):
    words = input().split()
    print(" ".join(word[::-1] for word in words))
