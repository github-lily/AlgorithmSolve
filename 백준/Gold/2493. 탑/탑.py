
import sys
input = sys.stdin.readline

N = int(input())
towers = [0] + list(map(int,input().split()))       # tower 1부터 시작

ans = [0]*(N+1)
stack = [N]
i = N-1
while i > -1 :
    while stack :
        cur = stack.pop()
        if towers[i] >= towers[cur] :
            ans[cur] = i
        else :
            stack.append(cur)
            break
    stack.append(i)
    i -= 1
        

print(" ".join(map(str,ans[1:])))