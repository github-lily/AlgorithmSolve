import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
M = int(input())
for _ in range(M) :
    i,j = map(int,input().split())
    ans = sum(lst[i-1 : j])
    print(ans)
