
import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N) :
    lst = list(map(int,input().split()))
    for i in range(N) :
        if len(q) < N :
            heapq.heappush(q,lst[i])
        else :
            if lst[i] > q[0] :
                heapq.heapreplace(q,lst[i])
    
print(q[0])

            