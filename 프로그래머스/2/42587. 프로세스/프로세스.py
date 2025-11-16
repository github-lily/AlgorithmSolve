from collections import deque

def solution(priorities, location):
    qu = deque()
    
    for i,p in enumerate(priorities) :
        qu.append((p,i))
        
    ans = 0

    while qu:
        cur = qu.popleft()
        if any(cur[0] < q[0] for q in qu):
            qu.append(cur)
        else:
            ans += 1
            if cur[1] == location:
                return ans
