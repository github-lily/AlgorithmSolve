N = int(input())
A = list(map(int,input().split()))


stack = []
ans = [-1] * N

for i in range(1, N) :
    # 오큰수 저장
    if A[i-1] < A[i] :
        ans[i-1] = A[i]
        while stack and A[stack[-1]] < A[i] :
            si = stack.pop()    # stack index
            ans[si] = A[i]    
    # 오큰수 없으면 저장해두기
    else :
        stack.append(i-1)

print(*ans)
    