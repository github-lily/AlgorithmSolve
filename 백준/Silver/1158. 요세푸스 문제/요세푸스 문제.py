from collections import deque

N,K = map(int,input().split())
q = deque(range(1,N+1))
result = []

while q :
    for _ in range(K-1) :
        q.append(q.popleft())
    result.append(q.popleft())

ans = '<{}>'.format(", ".join(map(str,result)))

print(ans)