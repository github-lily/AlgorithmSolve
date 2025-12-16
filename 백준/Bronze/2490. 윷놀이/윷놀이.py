import sys

mapping = {0: "E", 1: "A", 2: "B", 3: "C", 4: "D"}

for _ in range(3):
    arr = list(map(int, sys.stdin.readline().split()))
    zeros = arr.count(0)
    print(mapping[zeros])
