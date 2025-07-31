import sys
input = sys.stdin.readline


n,m = map(int,input().split())
arr1 = [list(map(int,input().split())) for _ in range(n)]

m,k = map(int,input().split())
arr2 = [list(map(int,input().split())) for _ in range(m)]

matrix = [[0]*k for _ in range(n)]

for i in range(n) :
    for j in range(k) :
        for x in range(m) :   
            matrix[i][j] += arr1[i][x] * arr2[x][j]

for row in matrix :
    print(*row)