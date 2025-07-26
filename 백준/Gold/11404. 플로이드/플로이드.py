import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

INF = int(1e9)
# 1번부터 시작
graph = [[INF] * (N+1) for _ in range(N+1)]

# 시작 == 도착 : 가중치 0
for k in range(1,N+1) :
    graph[k][k] = 0

# 간선 정보 입력
for _ in range(M) :
    s,e,v = map(int,input().split())
    # 노선이 여러개이므로 작은 값으로 저장
    if graph[s][e] >= v :
        graph[s][e] = v

for k in range(1,N+1) :
    for i in range(1,N+1) :
        for j in range(1,N+1) :
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,N+1) :
    for j in range(1,N+1) :
        if graph[i][j] == INF :
            print("0", end=" ")
        else :
            print(graph[i][j], end=" ")
    print()