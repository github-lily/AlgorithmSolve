import sys
input = sys.stdin.readline

from collections import deque

def bfs(start) :
    q = deque([start])
    v[start] = 1

    while q :
        c = q.popleft()
        for w in graph[c] :
            if v[w] == 0 :
                if v[c] == 1 :
                    v[w] = 2
                else :
                    v[w] = 1
                q.append(w)
            elif v[w] == v[c] :
                return False
    return True
    


T = int(input())    
for _ in range(T) :
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E) :
        u,v = list(map(int,input().split()))
        graph[v].append(u)
        graph[u].append(v)


    v = [0] * (V+1)

    for i in range(1,V+1) :
        if v[i] == 0 :
            ans = bfs(i)
            if not ans :
                print("NO")
                break
    if ans :
        print("YES")
