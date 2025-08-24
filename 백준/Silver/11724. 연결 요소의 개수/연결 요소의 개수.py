import sys
input = sys.stdin.readline

from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
cnt = 0

for _ in range(m) :
    u,v = list(map(int,input().split()))
    graph[u].append(v)
    graph[v].append(u)

v = [0] * (n+1)

def bfs(start) :
    q = deque([start])
    v[start] = 1
    while q :
        node = q.popleft()
        for w in graph[node] : 
            if v[w] == 0 :
                v[w] = 1
                q.append(w)



for i in range(1,n+1) :
    if v[i] == 0 :
        bfs(i)
        cnt += 1

print(cnt)
