import sys

input = sys.stdin.readline

n = int(input())
students = []
for _ in range(n):
    name, k, e, m = input().split()
    students.append((name, int(k), int(e), int(m)))

students.sort(key=lambda s: (-s[1], s[2], -s[3], s[0]))

print("\n".join(s[0] for s in students))
