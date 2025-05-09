import sys
input = sys.stdin.readline

N = int(input())
times = map(int,input().split())

Y = 0
M = 0

for time in times :
    Y += ((time // 30) + 1) * 10
    M += ((time // 60) + 1) * 15

if Y < M :
    print("Y", Y)
elif Y > M :
    print("M", M)
else :
    print("Y M", Y)