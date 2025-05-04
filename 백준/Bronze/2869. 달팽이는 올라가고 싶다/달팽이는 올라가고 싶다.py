import sys
input = sys.stdin.readline

A, B, V = map(int,input().split())

target = V-B

one_day = A-B

days = target // one_day

if target % one_day != 0 :
    days += 1


print(days)