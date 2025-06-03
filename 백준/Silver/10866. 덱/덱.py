

import sys
input = sys.stdin.readline

from collections import deque

q = deque()
N = int(input())
for _ in range(N) :
    cmd = input().split()
    # print(len(cmd))
    # print(cmd)
    # print(cmd[0])
    if cmd[0] == "push_front" :
        q.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back" :
        q.append(int(cmd[1]))
    elif cmd[0] == "pop_front" :
        if q :
            print(q.popleft())
        else :
            print(-1)
    elif cmd[0] == "pop_back" :
        if q :
            print(q.pop())
        else :
            print(-1)
    elif cmd[0] == "size" :
        print(len(q))
    elif cmd[0] == "empty" :
        if q :
            print(0)
        else :
            print(1)
    elif cmd[0] == "front" :
        if q :
            print(q[0])
        else :
            print(-1)
    elif cmd[0] == "back" :
        if q :
            print(q[-1])
        else :
            print(-1)
    else :
        print("해당없음")

