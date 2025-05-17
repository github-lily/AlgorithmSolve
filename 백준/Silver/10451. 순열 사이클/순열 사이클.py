import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for _ in range(T) :
    N = int(input())
    nums = list(map(int,input().split()))
    v = [0] * N


    q = deque()
    cycle = 0

    for i in range(N) :
        # 자기 자신 순환 
        if i+1 == v[i] :
            cycle += 1
            v[i] = 1

        elif v[i] == 0 :
            q.append(i+1)
            while q :
                c = q.popleft() 
                if v[c-1] == 0 :
                    q.append(nums[c-1])
                    v[c-1] = 1
                else :
                    cycle += 1

    print(cycle)
