import sys
input = sys.stdin.readline

N = int(input())
lst = set(map(int,input().split()))
ans = sorted(lst)
print(*ans)
