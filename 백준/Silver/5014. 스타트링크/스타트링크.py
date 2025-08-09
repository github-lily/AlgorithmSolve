
import sys
input = sys.stdin.readline

from collections import deque

def bfs(s, e) :
    q = deque()
    v = [0] * (F+1)

    q.append(s)
    v[s] = 1    # return 할 때는 -1 하기

    while q :
        c = q.popleft()

        if c == e :
            return v[c]-1
        
        # 2방향, 범위내, 미방문
        for k in (c+U, c-D) :
            if 1<=k<=F and v[k] == 0 :
                q.append(k)
                v[k] = v[c]+1

    # 목적지를 찾을 수 없을 때
    return "use the stairs"

F,S,G,U,D = map(int,input().split())

ans = bfs(S,G)
print(ans)
        