import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
q = deque()

for _ in range(N) :
    cmd = list(input().strip().split())
    req = cmd[0]
    # print(req)
    if req == 'push' :
        q.append(cmd[1])
    
    elif req == 'size' :
        print(len(q))
    
    else :
        if q :
            if req == 'pop' :
                print(q.popleft())

            elif req == 'empty' :
                print(0)
            elif req == 'front' :
                print(q[0])
            
            elif req == 'back' :
                print(q[-1])
        else :
            if req == 'empty' :
                print(1)
            else :
                print(-1)
            