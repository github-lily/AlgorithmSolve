import sys

input = sys.stdin.readline

n = int(input())
danced = {"ChongChong"}

for _ in range(n):
    a, b = input().split()
    if a in danced or b in danced:
        danced.add(a)
        danced.add(b)

print(len(danced))
