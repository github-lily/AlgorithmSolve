import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    lst = sorted(map(int,input().split()),reverse=True)
    print(lst[2])