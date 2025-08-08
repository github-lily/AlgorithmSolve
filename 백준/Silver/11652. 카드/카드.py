import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]

count = Counter(arr)
print(sorted(count.items(), key=lambda x: (-x[1], x[0]))[0][0])
