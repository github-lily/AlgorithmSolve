N,M = map(int,input().split())

if N > M :
    ans = (N-1) + ((M-1)*N)
else :
    ans = (M-1) + ((N-1)*M)

print(ans)