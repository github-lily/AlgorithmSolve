from collections import deque

def solution(n, wires):
    L = len(wires)
    graph = [[] for _ in range(n+1)]
    
    for s,e in wires :
        graph[s].append(e)
        graph[e].append(s)

    def bfs(cut1, cut2) :
        q = deque([1])
        v = [0] * (n+1)
        v[1] = 1
        cnt = 1
        
        while q :
            cur = q.popleft()
            
            for nxt in graph[cur] :
                # 끊어진 선 넘기기
                if (cur == x1 and nxt == x2) or (cur == x2 and nxt == x1) :
                    continue
                elif v[nxt] == 0 :
                    q.append(nxt)
                    v[nxt] = 1
                    cnt += 1
        
        return abs(n - cnt*2)
        
        
    # 최소값 찾기
    mn = n*2
    for i in range(L) :
        x1,x2 = wires[i]    # 끊을 선
        
        diff = bfs(x1,x2)
        if mn > diff :
            mn = diff
    
    return mn
        

        
                
    
    
    
